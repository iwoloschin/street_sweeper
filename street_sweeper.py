"""A simple utility to automatically generate street sweeping reminders."""
import argparse
import calendar
from datetime import datetime
from datetime import timedelta
from dateutil import tz

import holidays
import ics

from pkg_resources import get_distribution, DistributionNotFound
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass

days = {
    'Sun': calendar.SUNDAY,
    'Mon': calendar.MONDAY,
    'Tue': calendar.TUESDAY,
    'Wed': calendar.WEDNESDAY,
    'Thu': calendar.THURSDAY,
    'Fri': calendar.FRIDAY,
    'Sat': calendar.SATURDAY,
}


def generate_dates(args, week_parity, street_sweeping_day):
    """Return a list of street sweeping dates."""
    cal = calendar.Calendar()
    street_sweeping_dates = []

    for month_number in range(args.first, args.last + 1):
        month = cal.monthdayscalendar(args.year, month_number)
        month_dates = []
        for week in month:
            for day in week:
                if day:
                    if week.index(day) == days[street_sweeping_day]:
                        event = datetime(
                            args.year, month_number, day, hour=args.start, tzinfo=tz.tzlocal())
                        month_dates.append(event)

        while len(month_dates) > 4:
            month_dates.pop()

        if week_parity == 'odd':
            month_dates.remove(month_dates[3])
            month_dates.remove(month_dates[1])
        else:
            month_dates.remove(month_dates[2])
            month_dates.remove(month_dates[0])

        street_sweeping_dates.append(month_dates)

    for month in street_sweeping_dates:
        for event in month:
            if event.date() in holidays.UnitedStates():
                month.remove(event)

    return street_sweeping_dates


def generate_calendar(args, week_parity, street_sweeping_day, dates):
    """Generate an ICS Calendar and save to disk."""
    cal = ics.Calendar()

    for month in dates:
        for day in month:
            event = ics.Event()
            event.name = 'Street Sweeping'
            event.begin = day
            event.end = day + timedelta(hours=(args.end - args.start))
            cal.events.append(event)

    filename = '{}_{}_{}_street_sweeping.ics'.format(
        str(args.year), week_parity, street_sweeping_day)
    with open(filename, 'w') as ics_file:
        ics_file.writelines(cal)


def parse_args():
    """Parse CLI arguments and provide sane defaults."""
    parser = argparse.ArgumentParser(description='Generate street sweeping calendar events')
    parser.add_argument('-y', '--year', default=datetime.now().year)
    parser.add_argument(
        '-w', '--week', help='1st & 3rd (Odd) or 2nd & 4th (Even) Weeks?',  nargs='+',
        choices=['odd', 'even'], default=['odd', 'even'])
    parser.add_argument(
        '-d', '--day', help='Day of street sweeping',  nargs='+',
        choices=calendar.day_abbr[0:5], default=calendar.day_abbr[0:5])
    parser.add_argument(
        '-s', '--start', default=8, choices=range(24),
        help='Street sweeping start time (24 hr)')
    parser.add_argument(
        '-e', '--end', default=12, choices=range(24),
        help='Street sweeping end time (24 hr)')
    parser.add_argument(
        '-f', '--first', default=4, choices=range(1, 13),
        help='First month of the year when street sweeping begins')
    parser.add_argument(
        '-l', '--last', default=12, choices=range(1, 13),
        help='Last month of the year with street sweeping')
    parser.add_argument(
        '-v', '--version', help='Print version of street_sweeper', action='store_true')

    return parser.parse_args()


def main():
    """Main function for street_sweeper."""
    args = parse_args()

    if args.version:
        print(__version__)

    for week in args.week:
        for day in args.day:
            dates = generate_dates(args, week, day)
            generate_calendar(args, week, day, dates)

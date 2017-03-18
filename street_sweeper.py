#!/usr/bin/env python3

# Standard Python Libraries
import argparse
import calendar
from datetime import datetime, timedelta
from dateutil import tz

# 3rd Party Libraries
import holidays
import ics

days = {
    'Sun' : calendar.SUNDAY,
    'Mon' : calendar.MONDAY,
    'Tue' : calendar.TUESDAY,
    'Wed' : calendar.WEDNESDAY,
    'Thu' : calendar.THURSDAY,
    'Fri' : calendar.FRIDAY,
    'Sat' : calendar.SATURDAY,
}

def generate_dates(year, week_parity, street_sweeping_day):
    # Generate a list of street sweeping dates

    # Street sweeping in Somerville goes April 1st till December 31st
    starting_month = 4
    ending_month = 12

    est_edt = tz.tzlocal()
    cal = calendar.Calendar()
    street_sweeping_dates = []

    for month_number in range(starting_month, ending_month + 1):
        # print(cal.monthdayscalendar(2016, month))
        month = cal.monthdayscalendar(year, month_number)
        month_dates = []
        for week in month:
            for day in week:
                if day:
                    if week.index(day) == days[street_sweeping_day]:
                        event = datetime(year, month_number, day, hour=8, tzinfo=est_edt)
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

    # for month in street_sweeping_dates:
    #     for day in month:
    #         print(day)

    return street_sweeping_dates

def generate_calendar(year, week_parity, street_sweeping_day, dates):

    cal = ics.Calendar()

    for month in dates:
        for day in month:
            event = ics.Event()
            event.name = 'Street Sweeping'
            event.begin = day
            event.end = day + timedelta(hours=4)
            cal.events.append(event)

    # for event in cal.events:
    #     print(event)

    with open(str(year) + '_' + week_parity + '_' +
        street_sweeping_day + '_street_sweeping.ics', 'w') as ics_file:
        ics_file.writelines(cal)

def parse_args():

    parser = argparse.ArgumentParser(description='Generate street sweeping calendar events')
    parser.add_argument('-y', '--year', default=2016)
    parser.add_argument('-w', '--week', help='1st & 3rd (Odd) or 2nd & 4th (Even) Weeks?',  nargs='+',
        choices=['odd', 'even'], default=['odd', 'even'])
    parser.add_argument('-d', '--day', help='Day of street sweeping',  nargs='+',
        choices=calendar.day_abbr[0:5], default=calendar.day_abbr[0:5])
    parser.add_argument('-s', '--start', help='Street sweeping start time (24 hr)', default=8)
    parser.add_argument('-e', '--end', help='Street sweeping end time (24 hr)', default=12)

    return parser.parse_args()

def main():

    args = parse_args()

    for week in args.week:
        for day in args.day:
            dates = generate_dates(args.year, week, day)
            generate_calendar(args.year, week, day, dates)

    # dates = generate_dates(args)
    # generate_calendar(args, dates)

if __name__ == "__main__":
    main()

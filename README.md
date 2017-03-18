# Street Sweeper
This is a simple tool for those of us who have to park their car on the street and need a little reminder about when to move their car for street sweeping.  Currently Street Sweeper is designed to work well in [Somerville, MA](http://www.somervillema.gov/sweeping), but this could be easily extended to match more cities.  Street Sweeper will output a series of ICS files that can be easily imported into Google Calendar.

## Usage
```
$ ./street_sweeper.py -h
usage: street_sweeper.py [-h] [-y YEAR] [-w {odd,even} [{odd,even} ...]]
                         [-d {Mon,Tue,Wed,Thu,Fri} [{Mon,Tue,Wed,Thu,Fri} ...]]
                         [-s START] [-e END]

Generate street sweeping calendar events

optional arguments:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR
  -w {odd,even} [{odd,even} ...], --week {odd,even} [{odd,even} ...]
                        1st & 3rd (Odd) or 2nd & 4th (Even) Weeks?
  -d {Mon,Tue,Wed,Thu,Fri} [{Mon,Tue,Wed,Thu,Fri} ...], --day {Mon,Tue,Wed,Thu,Fri} [{Mon,Tue,Wed,Thu,Fri} ...]
                        Day of street sweeping
  -s START, --start START
                        Street sweeping start time (24 hr)
  -e END, --end END     Street sweeping end time (24 hr)
  ```

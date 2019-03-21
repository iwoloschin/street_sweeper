# Street Sweeper
This is a simple tool for those of us who have to park their car on the street and need a little reminder about when to move their car for street sweeping.  Currently Street Sweeper is designed to work well in [Somerville, MA](http://www.somervillema.gov/sweeping), but this could be easily extended to match more cities.  Street Sweeper will output a series of ICS files that can be easily imported into Google Calendar.

**WARNING**

The street_sweeper program is not maintained by the City of Somerville, MA.  Any bugs or omissions should be reported to this project's [issues](https://github.com/iwoloschin/street_sweeper/issues) page, not to Somerville 311.  Always double check posted signs before parking, any parking tickets received are always the responsibility of the vehicle owner.

**WARNING**

# Import ICS Files into Google Calendar
Pre-generated ICS files are available for Somerville, MA residents for standard 8am-12pm street sweeping schedule, covering the standard April to December street sweeping period.  There are ten generated files, "Odd" (First & Third day) & "Even" (Second & Fourth day) for each day of the week.  Somerville does not sweep streets on federal or state holidays or the Fifth weekday (if any) of the month.  Typically most streets in Somerville have a different schedule for each side of the street, so most folks will need to select two ICS files.  Look at the street signs outside for the best information on what the schedule is on your street, online resources may not always match and the street signs are assumed to always be correct.

The below instructions assume you already have a Google Account setup for yourself.  If you do not have a Google Account please set that up first.

**WARNING**

The pre-generated files may have errors, the vehicle owner must always double check against posted signage and is always responsible for any parking tickets that may be incurred.

**WARNING**

## Getting the ICS Files
The ICS files for 2019 can be found [here](https://github.com/iwoloschin/street_sweeper/tree/master/2019).  Pick the two that match your street, or more if you live near an area that has streets on different schedules.

## Creating a New Google Calendar
I've found street sweeping reminders work best in their own calendar, they get their own color on the main display and can have calendar specific notifications for all events by default.  This setup only needs to be done once, in the future this calendar can simply be reused.

In Google Calendar click on the gear icon on the top right and click "Settings".  In the Settings menu click "Add Calendar" and then "New Calendar".  Pick a name, such as "Street Sweeping", and enter a description if you'd like, then click "Create Calendar".

Your new calendar will now be on the left side, click on the new calendar's name and scroll down until you see "Event Notifications".  Add as many notifications as you'd like here, I've found 12 hours and 1 hour before street sweeping is a good reminder for me.

## Importing ICS Files into Your Calendar
Click the gear icon on the top right and click "Settings".  In the settings menu click the "Import & Export" button.  Select the first ICS file from your computer and pick the appropriate calendar to import into, then click the "Import" button.  Repeat for as many ICS files as you have to import.

# Generating Custom ICS Files
If you need different ICS files you can `pip3 install` it via git:
```
pip3 install git+https://github.com/iwoloschin/street_sweeper.git
```

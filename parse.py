import re
import datetime
import calendar

delimeter = ' +'
data = open('meiv2.data')

# Read first line (to know limits)
start_end = next(data)[:-1]
start, end = re.split(delimeter, start_end)
start, end = int(start), int(end)

month_data = []

# loop through file adding data to recovered
for year in range(start, end + 1):
    year_data = next(data)[:-1]
    YEAR, DJ, JF, FM, MA, AM, MJ, JJ, JA, AS, SO, ON, ND = re.split(delimeter, year_data)

    months = [DJ, JF, FM, MA, AM, MJ, JJ, JA, AS, SO, ON, ND]

    for index, value in enumerate(months):
        # parse value to relevant type
        if value != '-999.00':
            value = float(value)
        else:
            value = None
        # get last day of last month
        endmonth = index + 1
        _, lastday = calendar.monthrange(year, endmonth)
        enddate = datetime.date(year=year, month=endmonth, day=lastday)
        # move two months back
        if endmonth == 1:
            _, daysInPrevMonth = calendar.monthrange(year-1, 12)
        else:
            _, daysInPrevMonth = calendar.monthrange(year, endmonth-1)

        startdate = enddate - datetime.timedelta(days=(lastday+daysInPrevMonth)-1)
        # append to main data
        month_data.append(
            [startdate, enddate, value]
        )

month_data

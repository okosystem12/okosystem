from datetime import date

from Site.app.datetime.for_date import for_date


def bDate(day, month, year):
    if day == 0 or month == 0 or year == 0:
        return ''

    return for_date(date(year, month, day))

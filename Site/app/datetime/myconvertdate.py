from datetime import date, datetime

from Site.app.datetime.for_date import for_date


def myconvertdate(o):
    if isinstance(o, date) or isinstance(o, datetime):
        return for_date(o)

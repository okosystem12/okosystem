from datetime import datetime

from Site.app.datetime.for_datetime import for_datetime


def my_convert_datetime(o):
    if isinstance(o, datetime):
        return for_datetime(o)

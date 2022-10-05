from datetime import datetime, date
from django.utils import timezone


def myconvertdate(o):
    if isinstance(o, date) or isinstance(o, datetime):
        return for_date(o)


def for_date(self):
    if self is not None:
        try:
            return timezone.localtime(self).strftime("%Y-%m-%d").__str__()
        except Exception as e:
            return ''
    else:
        return ''


def my_convert_datetime(o):
    if isinstance(o, datetime):
        return for_datetime(o)


def for_datetime(self):
    if self is not None:
        return timezone.localtime(self).strftime("%Y-%m-%d %H:%M:%S").__str__()
    else:
        return ''
from django.utils import timezone


def for_datetime(self):
    if self is not None:
        return timezone.localtime(self).strftime("%Y-%m-%d %H:%M:%S")
    else:
        return ''

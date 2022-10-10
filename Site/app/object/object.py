from datetime import datetime


def objectRemoveAt(obj):
    for o in obj:
        o.removeAt = datetime.now()
        o.save()
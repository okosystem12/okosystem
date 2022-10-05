from datetime import datetime, date

from django.db.models import Q


def _obj(obj, key, default=''):
    return obj[key] if key in obj else default


def objDate(obj, key, default='T'):
    return _obj(obj, key, default).split('T')[0]


def objectRemoveAt(obj):
    for o in obj:
        o.removeAt = datetime.now()
        o.save()


def objectUpdate(obj, listVal, controlUser):
    for val in listVal:
        o = obj.objects.filter(Q(id=_obj(val, 'id'))).first()
        if not o:
            o = obj.objects.create()
        o.value = _obj(val, 'value', '')
        o.controlUser = controlUser
        o.save()
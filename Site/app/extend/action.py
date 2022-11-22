from threading import Thread

from django.db.models import Q

from Site.app.extend.fin import fin
from Site.models import CorruptInfo


def action(_id, a):
    Thread(target=action_t, args=[_id, a]).start()


def action_t(_id, a):
    _corrupt = CorruptInfo.objects.filter(Q(pk=_id)).first()
    if _corrupt:
        extList = []
        try:
            extList = a(_corrupt.value.lower())
        except Exception as e:
            print(e)

        fin(_id, extList)

from threading import Thread

from django.db.models import Q

from Site.models import CorruptInfo, CorruptExtend, CorruptExtendFin


def action(_id, a):
    Thread(target=action_t, args=[_id, a]).start()


def action_t(_id, a):
    _corrupt = CorruptInfo.objects.filter(Q(pk=_id) & Q(removeAt__isnull=True)).first()
    if _corrupt:
        extList = []
        _old_value = _corrupt.value.lower()
        try:
            extList = a(_old_value)
        except Exception as e:
            print(e)

        _corrupt = CorruptInfo.objects.filter(Q(pk=_id) & Q(removeAt__isnull=True)).first()
        if _corrupt and _old_value == _corrupt.value.lower():
            for ext in extList:
                CorruptExtend.objects.create(corruptInfo_id=_id, value=ext)
            _corrupt = CorruptInfo.objects.filter(Q(pk=_id) & Q(removeAt__isnull=True)).first()
            if _corrupt and _old_value == _corrupt.value.lower():
                CorruptExtendFin.objects.create(corruptInfo_id=_id, type=a.__name__, count=len(extList))
            else:
                CorruptExtend.objects.filter(Q(corruptInfo_id=_id) & Q(value__in=extList)).delete()
                CorruptExtendFin.objects.filter(Q(corruptInfo_id=_id) & Q(type=a.__name__)).delete()

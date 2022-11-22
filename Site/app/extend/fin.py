from django.db.models import Q

from Site.models import CorruptInfo, CorruptExtend


def fin(_id, extList):
    for ext in extList:
        CorruptExtend.objects.create(corruptInfo_id=_id, value=ext)
    _corrupt = CorruptInfo.objects.filter(Q(pk=_id)).first()
    _corrupt.extend_count += len(extList)
    _corrupt.extend_finish += 20
    _corrupt.save()

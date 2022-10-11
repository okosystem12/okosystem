from django.db.models import Q

from Site.models import Vch


def vchNumber(_id):
    if _id:
        vch = Vch.objects.filter(Q(removeAt=None) & Q(pk=_id)).first()
        if vch:
            return vch.number
    return ''

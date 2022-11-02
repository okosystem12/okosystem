from django.db.models import Q

from Site.app.object.elem import elem


def filter(oList, _data):
    _username = elem(_data, 'username')
    if _username != '':
        for word in _username.split(' '):
            oList = oList.filter(
                Q(lastName__icontains=word) | Q(firstName__icontains=word) | Q(patronymic__icontains=word))

    _vch = elem(_data, 'vch', [])
    if len(_vch):
        oList = oList.filter(Q(vch_id__in=_vch))

    return oList

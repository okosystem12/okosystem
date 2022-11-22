from django.db.models import Q

from Site.app.object.elem import elem


def filter(oList, _data):
    _username = elem(_data, 'username')
    if _username != '':
        oList = oList.filter(
            Q(lastName__icontains=_username) | Q(firstName__icontains=_username) | Q(patronymic__icontains=_username))

    _vch = elem(_data, 'vch', [])
    if len(_vch):
        oList = oList.filter(Q(vch_id__in=_vch))

    _status = elem(_data, 'status', [])
    if len(_status):
        oList = oList.filter(Q(status__id__in=_status))

    _social = elem(_data, 'social', [])
    if len(_social) == 1:
        if 0 in _social:
            oList = oList.filter(Q(social__confirmedAt__isnull=False))
        if 1 in _social:
            oList = oList.filter(Q(social__confirmedAt__isnull=True))

    return oList

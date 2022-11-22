from django.db.models import Q

from Site.app.object.elem import elem


def filter(oList, _data):
    _username = elem(_data, 'username')
    if _username != '':
        oList = oList.filter(
            Q(lastName__icontains=_username) | Q(firstName__icontains=_username) | Q(patronymic__icontains=_username))
    return oList

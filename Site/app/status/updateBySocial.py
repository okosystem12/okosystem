from django.db.models import Q

from Site.app.status.setStatus import setStatus
from Site.models import Social


def updateBySocial(_user, _type='manual'):
    _social_list = Social.objects.filter(Q(controlUser=_user))

    if _type == 'manual':
        if not _social_list.exists():
            setStatus(_user)
        elif not _social_list.filter(Q(confirmedAt__isnull=True)).exists():
            setStatus(_user, 'work')
    if _type == 'robot':
        if not _social_list.exists():
            setStatus(_user, 'prepare', 'notEqual')
        elif not _social_list.filter(Q(confirmedAt__isnull=False)).exists():
            setStatus(_user, 'prepare', 'equal')

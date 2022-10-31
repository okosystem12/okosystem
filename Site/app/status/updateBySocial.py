from django.db.models import Q

from Site.app.status.setStatus import setStatus
from Site.models import Social


def updateBySocial(_user):
    wasUpdate = False
    _social_list = Social.objects.filter(Q(controlUser=_user))
    if not _social_list.exists():
        setStatus(_user)
        wasUpdate = True
    elif not _social_list.filter(Q(confirmedAt__isnull=True)).exists():
        setStatus(_user, 'work')
        wasUpdate = True

    return wasUpdate

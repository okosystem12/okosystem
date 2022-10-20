from django.db.models import Q

from Site.app.status.updateBySocial import updateBySocial
from Site.models import Social


def unsetSocial(_user, _value):
    _socialList = Social.objects.filter(~Q(controlUser=_user) & Q(value=_value))

    for _social in _socialList:
        _cUser = _social.controlUser
        _social.delete()
        updateBySocial(_cUser)



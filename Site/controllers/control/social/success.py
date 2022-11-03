from django.db.models import Q

from Site.app.status.updateBySocial import updateBySocial
from Site.app.table.control.value import value
from Site.models import Social


def success(_user):
    updateBySocial(_user.first())
    return {
        'controlUser': value(_user),
        'socialList': list(Social.objects.filter(Q(controlUser=_user.first())).values()),
        'successText': 'Действие выполнено'
    }

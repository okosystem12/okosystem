from django.db.models import Q

from Site.models import Status


def setStatus(controlUser=None, _type='init'):
    if controlUser:
        status = Status.objects.filter(Q(type=_type)).first()

        if status:
            controlUser.status = status
            controlUser.save()

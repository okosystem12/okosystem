from django.db.models import Q

from Site.models import Status


def init():
    status = Status.objects.filter(Q(type='init'))


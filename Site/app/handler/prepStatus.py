from django.db.models import Q

from Site.models import Status


def prepStatus(_id=None):
    result = {}
    status = Status.objects.filter(Q(pk=_id)).first()
    if status:
        result.update(status.__dict__)
        result.update({
            'stage': status.stage.type,
            'title': f'{status.stage.name}: {status.name}'
        })
    return result

from django.db.models import Q

from Site.models import Status


def prepStatus(_id=None):
    result = {}
    status = Status.objects.filter(Q(pk=_id)).first()
    if status:
        result['value'] = status.value
        result['color'] = status.color
        result['title'] = status.stage.name + ': ' + status.name
        result['blockSearch'] = status.type == 'search'
        result['blockAnalysis'] = status.type == 'analysis'
    return result

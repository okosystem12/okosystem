from django.db.models import Q

from Site.app.handler.linkList import linklist
from Site.app.handler.valueList import valueList
from Site.models import GroupsCorrupt


def oneGroup(group, gc):
    return {
        'realId': group.id,
        'materialsType': 'Группа',
        'materials': {
            'type': 'group',
            'content': {
                'name': group.name,
            }
        },
        'social': linklist([group.social.prefix + group.social.value]),
        'controlUser': group.social.controlUser.fullName(),
        'corrupt': valueList(gc.values_list('corrupt__info', flat=True))
    }

from django.db.models import Q

from Site.app.handler.linkList import linklist
from Site.app.handler.valueList import valueList
from Site.app.social.groupLink import groupLink
from Site.models import GroupsCorrupt


def oneGroup(group):
    return {
        'realId': group.id,
        'materialsType': 'Сообщество',
        'materials': {
            'type': 'group',
            'content': {
                'name': group.name,
                'link': linklist([groupLink(group)])
            }
        }
    }

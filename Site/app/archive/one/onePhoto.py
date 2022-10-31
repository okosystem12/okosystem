from django.db.models import Q

from Site.app.handler.linkList import linklist
from Site.app.handler.valueList import valueList
from Site.models import PhotosCorrupt


def onePhoto(photo):
    return {
        'realId': photo.id,
        'materialsType': 'Фото',
        'materials': {
            'type': 'photo',
            'content': {
                'link': linklist([photo.link])
            }
        }
    }

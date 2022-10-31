from django.db.models import Q

from Site.app.handler.linkList import linklist
from Site.app.handler.valueList import valueList
from Site.models import VideoCorrupt


def oneVideo(video, vc):
    return {
        'realId': video.id,
        'materialsType': 'Видео',
        'materials': {
            'type': 'video',
            'content': {
                'text': video.name,
                'link': linklist([video.link])
            }
        },
        'social': linklist([video.social.prefix + video.social.value]),
        'controlUser': video.social.controlUser.fullName(),
        'corrupt': valueList(vc.values_list('corrupt__info', flat=True))
    }

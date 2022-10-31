from django.db.models import Q

from Site.app.handler.linkList import linklist
from Site.app.handler.valueList import valueList
from Site.app.social.postLink import postLink
from Site.models import PostCorrupt


def onePost(post, pc):
    return {
        'realId': post.id,
        'materialsType': 'Пост',
        'materials': {
            'type': 'post',
            'content': {
                'text': post.text,
                'link': linklist([postLink(post)])
            }
        },
        'social': linklist([post.social.prefix + post.social.value]),
        'controlUser': post.social.controlUser.fullName(),
        'corrupt': valueList(pc.values_list('corrupt__info', flat=True))
    }

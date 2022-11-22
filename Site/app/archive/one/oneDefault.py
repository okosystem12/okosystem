
from Site.app.handler.linkList import linklist
from Site.app.handler.valueList import valueList


def oneDefault(o, c):
    return {
        'social': linklist([o.social.prefix + o.social.value]),
        'controlUser_id': o.social.controlUser.id,
        'controlUser': o.social.controlUser.fullName(),
        'corrupt': valueList(c.values_list('corrupt__info', flat=True)),
        'corruptList': list(c.values('id', 'corrupt__info')),
        'confirmedAt': c.order_by('confirmedAt').first().confirmedAt
    }

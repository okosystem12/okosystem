from datetime import datetime

from django.db.models import Q

from Site.app.status.setStatus import setStatus
from Site.models import Social, Post, PostCorrupt, VideoCorrupt, PhotosCorrupt, GroupsCorrupt, InfCorrupt


def updateByAnalysis(_user, _type='manual'):
    _social_list = Social.objects.filter(Q(controlUser=_user))

    if _type == 'manual':
        if not _social_list.exists():
            setStatus(_user)
        elif not _social_list.filter(Q(confirmedAt__isnull=True)).exists():
            setStatus(_user, 'work', 'analysis')
    if _type == 'robot':
        _post = PostCorrupt.objects.filter(Q(post__social__in=_social_list) & Q(confirmedAt__isnull=False)).exists()
        _video = VideoCorrupt.objects.filter(Q(video__social__in=_social_list) & Q(confirmedAt__isnull=False)).exists()
        _photos = PhotosCorrupt.objects.filter(Q(photo__social__in=_social_list) & Q(confirmedAt__isnull=False)).exists()
        _groups = GroupsCorrupt.objects.filter(Q(groups__social__in=_social_list) & Q(confirmedAt__isnull=False)).exists()
        _inf = InfCorrupt.objects.filter(Q(inf__social__in=_social_list) & Q(confirmedAt__isnull=False)).exists()

        if _post or _video or _photos or _groups or _inf:
            setStatus(_user, 'work', 'warning')
        else:
            setStatus(_user, 'work', 'success')

        _user.lastAnalysisAt = datetime.now()
        _user.save()

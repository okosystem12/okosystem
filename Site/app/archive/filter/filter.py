from django.db.models import Q

from Site.app.object.elem import elem


def filter(postList, videoList, groupsList, photosList, infList, _data):
    _user = elem(_data, 'user', [])
    if len(_user):
        postList = postList.filter(Q(social__controlUser_id__in=_user))
        videoList = videoList.filter(Q(social__controlUser_id__in=_user))
        groupsList = groupsList.filter(Q(social__controlUser_id__in=_user))
        photosList = photosList.filter(Q(social__controlUser_id__in=_user))
        infList = infList.filter(Q(social__controlUser_id__in=_user))

    _corruptInfo = elem(_data, 'corruptInfo', [])
    if len(_corruptInfo):
        postList = postList.filter(Q(postcorrupt__corrupt_id__in=_corruptInfo))
        videoList = videoList.filter(Q(videocorrupt__corrupt_id__in=_corruptInfo))
        groupsList = groupsList.filter(Q(groupscorrupt__corrupt_id__in=_corruptInfo))
        photosList = photosList.filter(Q(photoscorrupt__corrupt_id__in=_corruptInfo))
        infList = infList.filter(Q(infcorrupt__corrupt_id__in=_corruptInfo))

    _corruptType = elem(_data, 'corruptType', [])
    if len(_corruptType):
        if not 0 in _corruptType:
            postList = postList.filter(Q(pk=None))
        if not 1 in _corruptType:
            videoList = videoList.filter(Q(pk=None))
        if not 2 in _corruptType:
            groupsList = groupsList.filter(Q(pk=None))
        if not 3 in _corruptType:
            photosList = photosList.filter(Q(pk=None))
        if not 4 in _corruptType:
            infList = infList.filter(Q(pk=None))

    return postList, videoList, groupsList, photosList, infList

from django.db.models import Q

from Site.app.archive.one.oneGroup import oneGroup
from Site.app.archive.one.oneInf import oneInf
from Site.app.archive.one.onePhoto import onePhoto
from Site.app.archive.one.onePost import onePost
from Site.app.archive.one.oneVideo import oneVideo
from Site.models import PostCorrupt, VideoCorrupt, GroupsCorrupt, PhotosCorrupt, InfCorrupt


def data(postList, videoList, groupsList, photosList, infList, confirmed=False):
    emptyRow = {'id': '', 'controlUser': '', 'materials': '', 'social': '', 'corrupt': '', 'materialsType': ''}
    index = 0
    result = []

    for post in postList.iterator():
        pc = PostCorrupt.objects.filter(Q(post_id=post.pk) & Q(confirmedAt__isnull=confirmed)).order_by('corrupt__info')
        if pc.exists():
            info = {}
            info.update(emptyRow)
            info.update({'id': index})
            info.update(onePost(post, pc))
            result.append(info)
            index += 1

    index += 1000
    for video in videoList.iterator():
        vc = VideoCorrupt.objects.filter(Q(video=video) & Q(confirmedAt__isnull=confirmed)).order_by('corrupt__info')
        if vc.exists():
            info = {}
            info.update(emptyRow)
            info.update({'id': index})
            info.update(oneVideo(video, vc))
            result.append(info)
            index += 1

    index += 1000
    for group in groupsList.iterator():
        gc = GroupsCorrupt.objects.filter(Q(groups_id=group.pk) & Q(confirmedAt__isnull=confirmed)).order_by(
            'corrupt__info')
        if gc.exists():
            info = {}
            info.update(emptyRow)
            info.update({'id': index})
            info.update(oneGroup(group, gc))
            result.append(info)
            index += 1

    index += 1000
    for photo in photosList.iterator():
        pc = PhotosCorrupt.objects.filter(Q(photo_id=photo.pk) & Q(confirmedAt__isnull=confirmed)).order_by(
            'corrupt__info')
        if pc.exists():
            info = {}
            info.update(emptyRow)
            info.update({'id': index})
            info.update(onePhoto(photo, pc))
            result.append(info)
            index += 1

    index += 1000
    for inf in infList.iterator():
        ic = InfCorrupt.objects.filter(Q(inf_id=inf.pk) & Q(confirmedAt__isnull=confirmed)).order_by('corrupt__info')
        if ic.exists():
            info = {}
            info.update(emptyRow)
            info.update({'id': index})
            info.update(oneInf(inf, ic))
            result.append(info)
            index += 1

    return result

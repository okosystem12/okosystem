from django.db.models import Q

from Site.app.archive.data import data
from Site.models import Post, Video, Groups, Photos, Inf


def corruptionList(controlUser):
    postList = Post.objects.filter(Q(social__controlUser__in=controlUser) & Q(postcorrupt__confirmedAt__isnull=True))
    postList = Post.objects.filter(Q(pk__in=postList.values_list('pk', flat=True)))

    videoList = Video.objects.filter(Q(social__controlUser__in=controlUser) & Q(videocorrupt__confirmedAt__isnull=True))
    videoList = Video.objects.filter(Q(pk__in=videoList.values_list('pk', flat=True)))

    groupsList = Groups.objects.filter(Q(social__controlUser__in=controlUser) & Q(groupscorrupt__confirmedAt__isnull=True))
    groupsList = Groups.objects.filter(Q(pk__in=groupsList.values_list('pk', flat=True)))

    photosList = Photos.objects.filter(Q(social__controlUser__in=controlUser) & Q(photoscorrupt__confirmedAt__isnull=True))
    photosList = Photos.objects.filter(Q(pk__in=photosList.values_list('pk', flat=True)))

    infList = Inf.objects.filter(Q(social__controlUser__in=controlUser) & Q(infcorrupt__confirmedAt__isnull=True))
    infList = Inf.objects.filter(Q(pk__in=infList.values_list('pk', flat=True)))

    return data(postList, videoList, groupsList, photosList, infList, True)

from django.db.models import Q

from Site.models import Post, Video, Groups, Photos, Inf


def main():
    postList = Post.objects.filter(Q(postcorrupt__confirmedAt__isnull=False))
    postList = Post.objects.filter(Q(pk__in=postList))

    videoList = Video.objects.filter(Q(videocorrupt__confirmedAt__isnull=False))
    videoList = Video.objects.filter(Q(pk__in=videoList))

    groupsList = Groups.objects.filter(Q(groupscorrupt__confirmedAt__isnull=False))
    groupsList = Groups.objects.filter(Q(pk__in=groupsList))

    photosList = Photos.objects.filter(Q(photoscorrupt__confirmedAt__isnull=False))
    photosList = Photos.objects.filter(Q(pk__in=photosList))

    infList = Inf.objects.filter(Q(infcorrupt__confirmedAt__isnull=False))
    infList = Inf.objects.filter(Q(pk__in=infList))

    return postList, videoList, groupsList, photosList, infList

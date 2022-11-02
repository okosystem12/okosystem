import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.archive.search.fJoin import fJoin
from Site.app.array.sortList import sortList
from Site.app.array.sortListCustom import sortListCustom
from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.archive.data import data
from Site.app.object.elem import elem
from Site.app.table.tableConfig import tableConfig
from Site.app.archive.order.corrupt import corrupt
from Site.app.archive.order.social import social
from Site.app.archive.filter.filter import filter
from Site.models import Post, Video, Groups, Photos, Inf


@csrf_exempt
def table(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    tc = tableConfig(request.POST)

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

    iTotalRecords = postList.count() + videoList.count() + groupsList.count() + photosList.count() + infList.count()

    _data = json.loads(elem(request.GET, 'data', '{}'))
    postList, videoList, groupsList, photosList, infList = filter(postList, videoList, groupsList, photosList, infList, _data)

    if tc['search'] != '':
        for word in tc['search'].split(' '):
            postList = postList.filter(
                fJoin(word)
                | (Q(postcorrupt__corrupt__info__icontains=word) & Q(postcorrupt__confirmedAt__isnull=False))
                | Q(text__icontains=word)
            )
            videoList = videoList.filter(
                fJoin(word)
                | (Q(videocorrupt__corrupt__info__icontains=word) & Q(videocorrupt__confirmedAt__isnull=False))
                | Q(name__icontains=word)
                | Q(link__icontains=word)
            )
            groupsList = groupsList.filter(
                fJoin(word)
                | (Q(groupscorrupt__corrupt__info__icontains=word) & Q(groupscorrupt__confirmedAt__isnull=False))
                | Q(name__icontains=word)
            )
            photosList = photosList.filter(
                fJoin(word)
                | (Q(photoscorrupt__corrupt__info__icontains=word) & Q(photoscorrupt__confirmedAt__isnull=False))
                | Q(link__icontains=word)
            )
            infList = infList.filter(
                fJoin(word)
                | (Q(infcorrupt__corrupt__info__icontains=word) & Q(infcorrupt__confirmedAt__isnull=False))
                | Q(about__icontains=word)
                | Q(activities__icontains=word)
                | Q(books__icontains=word)
                | Q(games__icontains=word)
                | Q(interests__icontains=word)
                | Q(movies__icontains=word)
                | Q(music__icontains=word)
                | Q(nickname__icontains=word)
                | Q(quotes__icontains=word)
                | Q(status__icontains=word)
                | Q(tv__icontains=word)
            )

    postList = Post.objects.filter(Q(pk__in=postList))
    videoList = Video.objects.filter(Q(pk__in=videoList))
    groupsList = Groups.objects.filter(Q(pk__in=groupsList))
    photosList = Photos.objects.filter(Q(pk__in=photosList))
    infList = Inf.objects.filter(Q(pk__in=infList))

    dataList = data(postList, videoList, groupsList, photosList, infList)

    iTotalDisplayRecords = len(dataList)

    if tc['column_list'][tc['order']] == 'materialsType':
        dataList = sortList(dataList, 'materialsType', tc['order_dir'] != '')
    if tc['column_list'][tc['order']] == 'corrupt':
        dataList = sortListCustom(dataList, corrupt, tc['order_dir'] != '')
    if tc['column_list'][tc['order']] == 'social':
        dataList = sortListCustom(dataList, social, tc['order_dir'] != '')
    if tc['column_list'][tc['order']] == 'controlUser':
        dataList = sortList(dataList, 'controlUser', tc['order_dir'] != '')

    dataList = dataList[tc['start']:(tc['length'] + tc['start'])]

    args = {
        "draw": tc['draw'],
        "iTotalRecords": iTotalRecords,
        "iTotalDisplayRecords": iTotalDisplayRecords,
        'data': dataList,
    }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

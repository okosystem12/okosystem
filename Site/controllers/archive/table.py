import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.archive.main import main
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
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))

    tc = tableConfig(request.POST)

    postList, videoList, groupsList, photosList, infList = main()

    iTotalRecords = postList.count() + videoList.count() + groupsList.count() + photosList.count() + infList.count()

    _data = json.loads(elem(request.GET, 'data', '{}'))
    postList, videoList, groupsList, photosList, infList = filter(postList, videoList, groupsList, photosList, infList, _data)

    if tc['search'] != '':
        postList = postList.filter(
            fJoin(tc['search'])
            | (Q(postcorrupt__corrupt__info__icontains=tc['search']) & Q(postcorrupt__confirmedAt__isnull=False))
            | (Q(postcorrupt__confirmedAt__icontains=tc['search']) & Q(postcorrupt__confirmedAt__isnull=False))
            | Q(text__icontains=tc['search'])
        )
        videoList = videoList.filter(
            fJoin(tc['search'])
            | (Q(videocorrupt__corrupt__info__icontains=tc['search']) & Q(videocorrupt__confirmedAt__isnull=False))
            | (Q(videocorrupt__confirmedAt__icontains=tc['search']) & Q(videocorrupt__confirmedAt__isnull=False))
            | Q(name__icontains=tc['search'])
            | Q(link__icontains=tc['search'])
        )
        groupsList = groupsList.filter(
            fJoin(tc['search'])
            | (Q(groupscorrupt__corrupt__info__icontains=tc['search']) & Q(groupscorrupt__confirmedAt__isnull=False))
            | (Q(groupscorrupt__confirmedAt__icontains=tc['search']) & Q(groupscorrupt__confirmedAt__isnull=False))
            | Q(name__icontains=tc['search'])
        )
        photosList = photosList.filter(
            fJoin(tc['search'])
            | (Q(photoscorrupt__corrupt__info__icontains=tc['search']) & Q(photoscorrupt__confirmedAt__isnull=False))
            | (Q(photoscorrupt__confirmedAt__icontains=tc['search']) & Q(photoscorrupt__confirmedAt__isnull=False))
            | Q(link__icontains=tc['search'])
        )
        infList = infList.filter(
            fJoin(tc['search'])
            | (Q(infcorrupt__corrupt__info__icontains=tc['search']) & Q(infcorrupt__confirmedAt__isnull=False))
            | (Q(infcorrupt__confirmedAt__icontains=tc['search']) & Q(infcorrupt__confirmedAt__isnull=False))
            | Q(about__icontains=tc['search'])
            | Q(activities__icontains=tc['search'])
            | Q(books__icontains=tc['search'])
            | Q(games__icontains=tc['search'])
            | Q(interests__icontains=tc['search'])
            | Q(movies__icontains=tc['search'])
            | Q(music__icontains=tc['search'])
            | Q(nickname__icontains=tc['search'])
            | Q(quotes__icontains=tc['search'])
            | Q(status__icontains=tc['search'])
            | Q(tv__icontains=tc['search'])
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
    if tc['column_list'][tc['order']] == 'confirmedAt':
        dataList = sortList(dataList, 'confirmedAt', tc['order_dir'] != '')

    dataList = dataList[tc['start']:(tc['length'] + tc['start'])]

    args = {
        "draw": tc['draw'],
        "iTotalRecords": iTotalRecords,
        "iTotalDisplayRecords": iTotalDisplayRecords,
        'data': dataList,
    }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.array.sortList import sortList
from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.table.tableConfig import tableConfig
from Site.controllers.place.prepInfo import prepInfo
from Site.models import Countries, Regions, Cities


@csrf_exempt
def place_table(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    tc = tableConfig(request.POST)

    countriesList = Countries.objects.filter(Q(removeAt=None))
    regionsList = Regions.objects.filter(Q(removeAt=None) & Q(country__in=countriesList))
    citiesList = Cities.objects.filter(Q(removeAt=None) & (Q(region__in=regionsList) | Q(country__in=countriesList)))

    iTotalRecords = countriesList.count() + regionsList.count() + citiesList.count()

    if tc['search'] != '':
        for word in tc['search'].split(' '):
            countriesList = countriesList.filter(Q(title__icontains=word))
            regionsList = regionsList.filter(Q(title__icontains=word) | Q(country__in=countriesList))
            citiesList = citiesList.filter(
                Q(title__icontains=word) | (Q(region__in=regionsList) | Q(country__in=countriesList)))

    iTotalDisplayRecords= countriesList.count() + regionsList.count() + citiesList.count()

    allIn = prepInfo(countriesList, regionsList, citiesList)

    if tc['column_list'][tc['order']] == 'country':
        allIn = sortList(allIn, 'country', tc['order_dir'] != '')
    elif tc['column_list'][tc['order']] == 'region':
        allIn = sortList(allIn, 'region', tc['order_dir'] != '')
    elif tc['column_list'][tc['order']] == 'city':
        allIn = sortList(allIn, 'city', tc['order_dir'] != '')

    allIn = allIn[tc['start']:(tc['length'] + tc['start'])]

    args = {
        "draw": tc['draw'],
        "iTotalRecords": iTotalRecords,
        "iTotalDisplayRecords": iTotalDisplayRecords,
        'data': allIn,
    }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

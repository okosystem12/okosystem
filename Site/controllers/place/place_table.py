import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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

    allIn = prepInfo(countriesList, regionsList, citiesList)
    args = {
        "draw": tc['draw'],
        "iTotalRecords": len(allIn),
        "iTotalDisplayRecords": len(allIn),
        'data': allIn,
    }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

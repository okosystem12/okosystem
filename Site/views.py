from datetime import datetime

from django.db.models import Q
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from Site.models import AllUsersVK


@csrf_exempt
def index(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    # return render(request, 'Site/index.html')

    print(datetime.now())
    id_user_list_max = []
    pos = 0
    step = 1000000
    # while True:
    #     notAll = AllUsersVK.objects.all()[pos:pos + step]
    #     notAllList = notAll.values_list('id_user', flat=True)
    #     if len(notAllList) == 0:
    #         break
    #     id_user_list_max.append(max(notAllList))
    #     pos += step
    #     print(pos)
    # print(max(id_user_list_max))
    print(datetime.now())

    return render(request, 'Site/control.html')


@csrf_exempt
def control(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    return render(request, 'Site/control.html')


@csrf_exempt
def archive(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    return render(request, 'Site/archive.html')


@csrf_exempt
def corrupt(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    return render(request, 'Site/corrupt.html')


@csrf_exempt
def actions(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    return render(request, 'Site/actions.html')


@csrf_exempt
def reports(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    return render(request, 'Site/reports.html')


@csrf_exempt
def config(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    return render(request, 'Site/config/config.html')


@csrf_exempt
def place(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    return render(request, 'Site/config/place.html')


@csrf_exempt
def vch(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    return render(request, 'Site/config/vch.html')


@csrf_exempt
def tester(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    return render(request, 'Site/tester.html')


@csrf_exempt
def login(request):
    return render(request, 'Site/login.html')

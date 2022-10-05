from django.http import HttpResponse
import json

from django.shortcuts import render, redirect
from django.contrib import auth

from django.views.decorators.csrf import csrf_exempt

from Site.app.convertdate import *
from Site.app.file import *
from Site.app.object import _obj, objDate, objectRemoveAt, objectUpdate
from Site.models import *
from Site.view.place import placeObject


@csrf_exempt
def index(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    # return render(request, 'Site/index.html')
    return render(request, 'Site/control/control.html')


@csrf_exempt
def control(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    return render(request, 'Site/control/control.html')


@csrf_exempt
def control_info(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    controlUserList = ControlUser.objects.filter(Q(removeAt=None))
    controlUserImgList = ControlUserImg.objects.filter(Q(removeAt=None) & Q(controlUser__in=controlUserList))
    fileList = File.objects.filter(Q(removeAt=None) & Q(controluserimg__in=controlUserImgList))
    phoneList = Phone.objects.filter(Q(removeAt=None) & Q(controlUser__in=controlUserList))
    mailList = Mail.objects.filter(Q(removeAt=None) & Q(controlUser__in=controlUserList))
    placeList = Place.objects.all()

    args = {
        'fileList': list(fileList.values()),
        'controlUserImgList': list(controlUserImgList.values()),
        'controlUserList': list(controlUserList.values()),
        'phoneList': list(phoneList.values()),
        'mailList': list(mailList.values()),
        'placeList': list(placeList.values()),
    }

    args.update(placeObject())

    return HttpResponse(json.dumps(args, default=my_convert_datetime))


@csrf_exempt
def control_work(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    args = {}
    if request.POST:
        _data = json.loads(_obj(request.POST, 'data', '{}'))
        id = _obj(_data, 'id', None)

        _new = False
        controlUser = ControlUser.objects.filter(Q(pk=id)).first()
        if not controlUser:
            _new = True
            controlUser = ControlUser.objects.create()

        birthDate = objDate(_data, 'birthDate', '0.0.0').split('.')

        controlUser.lastName = _obj(_data, 'lastName')
        controlUser.firstName = _obj(_data, 'firstName')
        controlUser.patronymic = _obj(_data, 'patronymic')
        controlUser.birthDay = birthDate[0]
        controlUser.birthMonth = birthDate[1]
        controlUser.birthYear = birthDate[2]
        controlUser.updatedAt = datetime.now()

        birthCountry = _obj(_data, 'birthCountry')
        birthRegion = _obj(_data, 'birthRegion')
        birthCity = _obj(_data, 'birthCity')

        if birthCountry or birthRegion or birthCity:
            birthPlace = Place.objects.create(
                country_id=birthCountry,
                region_id=birthRegion,
                city_id=birthCity,
            )
            controlUser.birthPlace = birthPlace
        controlUser.save()

        for file in File.objects.filter(Q(pk__in=_obj(_data, 'photoList', []))):
            isDuplicate = ControlUserImg.objects.filter(Q(file=file)).count() != 0
            if not isDuplicate:
                ControlUserImg.objects.create(
                    controlUser=controlUser,
                    file=file
                )

        userPhoneList = Phone.objects.filter(Q(controlUser=controlUser))
        objectRemoveAt(userPhoneList.exclude(Q(id__in=_obj(_data, 'phoneIdList', []))))
        objectUpdate(Phone, _obj(_data, 'phoneList', []), controlUser)

        userMailList = Mail.objects.filter(Q(controlUser=controlUser))
        objectRemoveAt(userMailList.exclude(Q(id__in=_obj(_data, 'mailIdList', []))))
        objectUpdate(Mail, _obj(_data, 'mailList', []), controlUser)

        controlUserList = ControlUser.objects.filter(Q(removeAt=None) & Q(pk=controlUser.pk))
        controlUserImgList = ControlUserImg.objects.filter(Q(removeAt=None) & Q(controlUser__in=controlUserList))
        fileList = File.objects.filter(Q(removeAt=None) & Q(controluserimg__in=controlUserImgList))
        phoneList = Phone.objects.filter(Q(removeAt=None) & Q(controlUser__in=controlUserList))
        mailList = Mail.objects.filter(Q(removeAt=None) & Q(controlUser__in=controlUserList))
        placeList = Place.objects.all()

        args = {
            'successText': 'Запись добавлена' if _new else 'Запись обновлена',
            'fileList': list(fileList.values()),
            'controlUserImgList': list(controlUserImgList.values()),
            'controlUserList': list(controlUserList.values()),
            'phoneList': list(phoneList.values()),
            'mailList': list(mailList.values()),
            'placeList': list(placeList.values()),
        }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))


@csrf_exempt
def control_work_img(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    img = _obj(request.FILES, 'file')
    file = File.objects.create(
        name=img.name,
        file=img,
    )

    args = {
        'id': file.id,
        'name': file.name,
        'data': file.file.url,
    }
    return HttpResponse(json.dumps(args, default=my_convert_datetime))


@csrf_exempt
def control_work_img_remove(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    args = {}
    if request.POST:
        _data = json.loads(_obj(request.POST, 'data', '{}'))
        _id = _obj(_data, 'id', [])
        _controlUserId = _obj(_data, 'controlUserId', None)

        controlUser = ControlUser.objects.filter(Q(pk=_controlUserId)).first()

        if controlUser:
            objectRemoveAt(ControlUserImg.objects.filter(Q(file_id__in=_id)))
            objectRemoveAt(File.objects.filter(Q(id__in=_id)))
        else:
            hardRemoveFile(_id, File)

        args['successText'] = 'Файл удалён'
        args['reload'] = True
    return HttpResponse(json.dumps(args, default=my_convert_datetime))


@csrf_exempt
def control_remove(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    args = {}
    if request.POST:
        _data = json.loads(_obj(request.POST, 'data', '{}'))
        _id = _obj(_data, 'id', None)
        objectRemoveAt(ControlUser.objects.filter(Q(pk=_id)))

        args['successText'] = 'Запись удалена'
        args['reload'] = True
    return HttpResponse(json.dumps(args, default=my_convert_datetime))


@csrf_exempt
def table_info(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    args = {}
    if request.POST:
        _data = json.loads(_obj(request.POST, 'data', '{}'))
        table = _obj(_data, 'table')

        columnsList = Column.objects.filter(Q(table__type=table)).order_by('-fixed', 'order', 'pk')

        if columnsList.count() != 0:
            renderList = Render.objects.filter(Q(column__in=columnsList))
            patternList = PatternTable.objects.filter(Q(table__type=table))
            patternColumnsList = PatternColumn.objects.filter(Q(pattern__in=patternList))

            args = {
                'columnsList': list(columnsList.values()),
                'renderList': list(renderList.values()),
                'patternList': list(patternList.values()),
                'patternColumnsList': list(patternColumnsList.values()),
            }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))


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
def place_info(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    _data = json.loads(_obj(request.POST, 'data', '{}'))
    _type = _obj(_data, 'type')

    return HttpResponse(json.dumps(placeObject(_type), default=my_convert_datetime))


@csrf_exempt
def place_countries_work(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    args = {}
    if request.POST:
        _data = json.loads(_obj(request.POST, 'data', '{}'))
        id = _obj(_data, 'id', None)
        title = _obj(_data, 'title')

        if Countries.objects.filter(Q(removeAt=None) & Q(title=title)).exclude(Q(pk=id)).count() == 0:
            _new = False
            country = Countries.objects.filter(Q(removeAt=None) & Q(pk=id)).first()
            if not country:
                _new = True
                country = Countries.objects.create()

            country.title = title
            country.save()

            countriesList = Countries.objects.filter(Q(removeAt=None) & Q(pk=country.pk))

            args = {
                'successText': 'Запись обновлена' if _new else 'Запись добавлена',
                'countriesList': list(countriesList.values()),
            }
        else:
            args = {
                'errorText': 'Страна с названием "' + title + '" уже присутствует в системе',
            }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))


@csrf_exempt
def place_countries_remove(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    args = {}
    if request.POST:
        _data = json.loads(_obj(request.POST, 'data', '{}'))
        _id = _obj(_data, 'id')
        objectRemoveAt(Countries.objects.filter(Q(removeAt=None) & Q(pk=_id)))

        args['successText'] = 'Запись удалена'
    return HttpResponse(json.dumps(args, default=my_convert_datetime))


@csrf_exempt
def place_regions_work(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    args = {}
    if request.POST:
        _data = json.loads(_obj(request.POST, 'data', '{}'))
        id = _obj(_data, 'id', None)
        country_id = _obj(_data, 'country_id', None)
        title = _obj(_data, 'title')
        country = Countries.objects.filter(Q(removeAt=None) & Q(pk=country_id)).first()
        if country:
            if Regions.objects.filter(Q(removeAt=None) & Q(country=country) & Q(title=title)).exclude(
                    Q(pk=id)).count() == 0:
                _new = False
                region = Regions.objects.filter(Q(removeAt=None) & Q(pk=id)).first()
                if not region:
                    _new = True
                    region = Regions.objects.create()

                region.country = country
                region.title = title
                region.save()

                regionsList = Regions.objects.filter(Q(removeAt=None) & Q(pk=region.pk))

                args = {
                    'successText': 'Запись обновлена' if _new else 'Запись добавлена',
                    'regionsList': list(regionsList.values()),
                }
            else:
                args = {
                    'errorText': 'Регион с названием "' + title + '" для страны "' + country.title + '" уже присутствует в системе',
                }
        else:
            args = {
                'errorText': 'Ошибка',
            }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))


@csrf_exempt
def place_regions_remove(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    args = {}
    if request.POST:
        _data = json.loads(_obj(request.POST, 'data', '{}'))
        _id = _obj(_data, 'id')

        objectRemoveAt(Regions.objects.filter(Q(removeAt=None) & Q(pk=_id)))

        args['successText'] = 'Запись удалена'
    return HttpResponse(json.dumps(args, default=my_convert_datetime))


@csrf_exempt
def place_city_work(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    args = {}
    if request.POST:
        _data = json.loads(_obj(request.POST, 'data', '{}'))
        id = _obj(_data, 'id', None)
        country_id = _obj(_data, 'country_id', None)
        region_id = _obj(_data, 'region_id', None)
        title = _obj(_data, 'title')
        country = Countries.objects.filter(Q(removeAt=None) & Q(pk=country_id)).first()
        if country:
            region = Regions.objects.filter(Q(removeAt=None) & Q(pk=region_id)).first()
            if Cities.objects.filter(
                    Q(removeAt=None) & Q(country=country) & Q(region=region) & Q(title=title)).exclude(
                Q(pk=id)).count() == 0:
                _new = False
                city = Cities.objects.filter(Q(removeAt=None) & Q(pk=id)).first()
                if not city:
                    _new = True
                    city = Cities.objects.create()

                city.country = country
                city.region = region
                city.title = title
                city.save()

                citiesList = Cities.objects.filter(Q(removeAt=None) & Q(pk=city.pk))

                args = {
                    'successText': 'Запись обновлена' if _new else 'Запись добавлена',
                    'citiesList': list(citiesList.values()),
                }
            else:
                args = {
                    'errorText': 'Город с названием "'
                                 + title
                                 + '" для страны "'
                                 + country.title
                                 + (('" и региона "' + region.title) if region else '')
                                 + '" уже присутствует в системе',
                }
        else:
            args = {
                'errorText': 'Ошибка',
            }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))


@csrf_exempt
def place_city_remove(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    args = {}
    if request.POST:
        _data = json.loads(_obj(request.POST, 'data', '{}'))
        _id = _obj(_data, 'id')

        objectRemoveAt(Cities.objects.filter(Q(removeAt=None) & Q(pk=_id)))

        args['successText'] = 'Запись удалена'
    return HttpResponse(json.dumps(args, default=my_convert_datetime))


@csrf_exempt
def vch(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    return render(request, 'Site/config/vch.html')


@csrf_exempt
def vch_info(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    vchList = Vch.objects.filter(Q(removeAt=None))

    args = {
        'vchList': list(vchList.values()),
    }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))


@csrf_exempt
def vch_work(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    args = {}
    if request.POST:
        _data = json.loads(_obj(request.POST, 'data', '{}'))
        id = _obj(_data, 'id', None)
        number = _obj(_data, 'number')

        if Vch.objects.filter(Q(removeAt=None) & Q(number=number)).exclude(Q(pk=id)).count() == 0:
            _new = False
            _vch = Vch.objects.filter(Q(removeAt=None) & Q(pk=id)).first()
            if not _vch:
                _new = True
                _vch = Vch.objects.create()

            _vch.number = number
            _vch.save()

            vchList = Vch.objects.filter(Q(removeAt=None) & Q(pk=_vch.pk))

            args = {
                'successText': 'Запись обновлена' if _new else 'Запись добавлена',
                'vchList': list(vchList.values()),
            }
        else:
            args = {
                'errorText': 'ВЧ с номером "' + number + '" уже присутствует в системе',
            }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))


@csrf_exempt
def vch_remove(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    args = {}
    if request.POST:
        _data = json.loads(_obj(request.POST, 'data', '{}'))
        _id = _obj(_data, 'id')

        objectRemoveAt(Vch.objects.filter(Q(removeAt=None) & Q(pk=_id)))

        args['successText'] = 'Запись удалена'
    return HttpResponse(json.dumps(args, default=my_convert_datetime))


@csrf_exempt
def tester(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    return render(request, 'Site/tester.html')


@csrf_exempt
def login(request):
    return render(request, 'Site/login.html')


# Авторизация
@csrf_exempt
def auth_login(request):
    args = {}
    _data = json.loads(_obj(request.POST, 'data', '{}'))
    username = _obj(_data, 'username')
    password = _obj(_data, 'password')
    path = _data['path'] if 'path' in _data else '/'
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        args['redirect'] = path
    else:
        args['errorText'] = "Неправильный логин или пароль"

    return HttpResponse(json.dumps(args, default=my_convert_datetime))


# Деавторизация
@csrf_exempt
def auth_logout(request):
    auth.logout(request)
    return redirect('/')

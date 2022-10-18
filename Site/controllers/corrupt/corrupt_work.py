import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.object.elem import elem
from Site.models import CorruptInfo


@csrf_exempt
def corrupt_work(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        id = elem(_data, 'id', None)
        value = elem(_data, 'value')
        info = elem(_data, 'info')

        if CorruptInfo.objects.filter(Q(removeAt=None) & Q(value=value)).exclude(Q(pk=id)).count() == 0:
            _new = False
            _corrupt = CorruptInfo.objects.filter(Q(removeAt=None) & Q(pk=id)).first()
            if not _corrupt:
                _new = True
                _corrupt = CorruptInfo.objects.create()

            _corrupt.value = value
            _corrupt.info = info
            _corrupt.save()

            args = {
                'successText': 'Запись обновлена' if _new else 'Запись добавлена',
            }
        else:
            args = {
                'errorText': 'Ключевое слово "' + value + '" уже присутствует в системе',
            }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.corrupt.extend import extend
from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.log.log import log
from Site.app.object.elem import elem
from Site.app.text.inflect import inflect
from Site.app.text.repl.replAllType import replAllType
from Site.models import CorruptInfo, CorruptExtend, CorruptExtendFin


@csrf_exempt
def corrupt_work(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))

    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        id = elem(_data, 'id', None)
        value = elem(_data, 'value')
        info = elem(_data, 'info')
        _old_value = ''
        if CorruptInfo.objects.filter(Q(removeAt=None) & Q(value=value)).exclude(Q(pk=id)).count() == 0:
            _new = False
            _corrupt = CorruptInfo.objects.filter(Q(removeAt=None) & Q(pk=id)).first()
            if not _corrupt:
                _new = True
                _corrupt = CorruptInfo.objects.create()
            else:
                _old_value = _corrupt.value

            _corrupt.value = value
            _corrupt.info = info
            _corrupt.save()

            if _corrupt.value != _old_value:
                CorruptExtend.objects.filter(Q(corruptInfo=_corrupt)).delete()
                CorruptExtendFin.objects.filter(Q(corruptInfo=_corrupt)).delete()

                CorruptExtend.objects.create(corruptInfo=_corrupt, value=value.lower())
                CorruptExtendFin.objects.create(corruptInfo=_corrupt, type='default', count=1)

                extend(_corrupt.pk)

            log(request.user.pk, 'Ключевые слова', 'Изменение' if not _new else 'Создание', '')

            args = {
                'successText': 'Запись обновлена' if not _new else 'Запись добавлена',
            }
        else:
            args = {
                'errorHighlight': 'Ключевое слово "' + value + '" уже присутствует в системе',
            }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

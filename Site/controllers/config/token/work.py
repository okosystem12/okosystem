import json

from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.log.log import log
from Site.app.object.elem import elem
from Site.models import TokenAdmin
from genering_profils_vk.src.func import check_access_token


@csrf_exempt
def work(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout': True}, default=my_convert_datetime))

    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        tokenVK = elem(_data, 'tokenVK')

        _is_correct = check_access_token(tokenVK)

        if not elem(_is_correct, 'error', False):
            _token = TokenAdmin.objects.first()
            _old = _token.tokenVK
            _token.tokenVK = tokenVK
            _token.save()

            log(request.user.pk, 'Настройки', 'Токен администратора', 'Изменение', _old)

            args = {'successText': 'Токен администратора сохранён' }
        else:
            args = {'errorHighlight': 'Токен администратора не действителен'}

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

import json

from django.contrib import auth
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.object.elem import elem


@csrf_exempt
def auth_login(request):
    args = {}
    _data = json.loads(elem(request.POST, 'data', '{}'))
    username = elem(_data, 'username')
    password = elem(_data, 'password')
    path = _data['path'] if 'path' in _data else '/'
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        args['redirect'] = path
    else:
        args['errorText'] = "Неправильный логин или пароль"

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

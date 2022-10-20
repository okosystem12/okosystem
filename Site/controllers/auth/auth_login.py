import json

from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Q
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
        checkUser = User.objects.filter(Q(username=username)).first()
        if checkUser:
            args['errorPasswordHighlight'] = "Неправильный пароль"
        else:
            args['errorUsernameHighlight'] = "Неправильный логин"

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

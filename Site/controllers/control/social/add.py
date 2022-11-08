import json
from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.object.elem import elem
from Site.app.social.unsetSocial import unsetSocial
from Site.app.status.setStatus import setStatus
from Site.app.status.updateBySocial import updateBySocial
from Site.controllers.control.social.success import success
from Site.models import Social, ControlUser


@csrf_exempt
def add(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))
    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        _userId = elem(_data, 'userId', None)
        _value = elem(_data, 'value')

        _controlUser = ControlUser.objects.filter(Q(pk=_userId))

        if _controlUser.exists():
            _user = _controlUser.first()
            _check_value = Social.objects.filter(Q(value=_value) & Q(confirmedAt__isnull=False)).first()
            if not _check_value:
                _social = Social.objects.filter(Q(controlUser=_user) & Q(value=_value) & Q(confirmedAt__isnull=True)).first()
                if not _social:
                    _social = Social.objects.create(
                        controlUser=_user,
                        value=_value,
                        confirmedAt=datetime.now()
                    )

                _social.confirmedAt = datetime.now()
                _social.save()

                unsetSocial(_user, _value)
                args.update({'reloadTable': True})
            else:
                return HttpResponse(json.dumps({
                    'errorHighlight':
                        'Соц.сеть закреплена за пользователем ' +_check_value.controlUser.shortName()
                }, default=my_convert_datetime))

            args.update(success(_controlUser))
        else:
            return HttpResponse(json.dumps({'warningText': 'Действие не выполнено'}, default=my_convert_datetime))
    return HttpResponse(json.dumps(args, default=my_convert_datetime))

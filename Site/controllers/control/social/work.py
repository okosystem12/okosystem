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
from Site.models import Social, ControlUser


@csrf_exempt
def work(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))
    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        _id = elem(_data, 'id', None)
        _action = elem(_data, 'action', None)
        _userId = elem(_data, 'userId', None)
        _value = elem(_data, 'value')

        _user = ControlUser.objects.filter(Q(pk=_userId)).first()

        if _user:
            _social = Social.objects.filter(Q(pk=_id) | (Q(controlUser=_user) & Q(value=_value))).first()
            if not _social:
                if _action == 'add':
                    _check_value = Social.objects.filter(Q(value=_value) & Q(confirmedAt__isnull=False)).first()
                    if not _check_value:
                        _social = Social.objects.create(
                            controlUser=_user,
                            value=_value,
                            confirmedAt=datetime.now()
                        )
                        unsetSocial(_user, _value)
                        args.update({
                            'socialList': list(Social.objects.filter(Q(controlUser=_user)).values()),
                            'reloadTable': True
                        })
                    else:
                        return HttpResponse(json.dumps({
                            'errorHighlight':
                                'Соц.сеть закреплена за пользователем ' +_check_value.controlUser.shortName()
                        }, default=my_convert_datetime))
            else:
                if _action == 'confirm' or _social.value == _value:
                    _social.confirmedAt = datetime.now()
                    _social.save()
                    args.update({'reloadTable': True})
                    unsetSocial(_user, _social.value)
                    if _social.value == _value:
                        args.update({'socialList': list(Social.objects.filter(Q(controlUser=_user)).values())})

                if _action == 'reject':
                    if _social.confirmedAt:
                        args.update({'reloadTable': True})
                    _social.delete()

            args.update({
                'closeModal': updateBySocial(_user),
                'successText': 'Действие выполнено'
            })
        else:
            return HttpResponse(json.dumps({'warningText': 'Действие не выполнено'}, default=my_convert_datetime))
    return HttpResponse(json.dumps(args, default=my_convert_datetime))

import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.object.elem import elem
from Site.models import Post


@csrf_exempt
def post(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        _id = elem(_data, 'id')

        Post.objects.filter(Q(pk=_id)).delete()

        args['successText'] = 'Запись удалена'
    return HttpResponse(json.dumps(args, default=my_convert_datetime))

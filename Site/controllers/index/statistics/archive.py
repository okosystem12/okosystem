import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from Site.app.archive.main import main
from Site.app.datetime.my_convert_datetime import my_convert_datetime


@csrf_exempt
def archive(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))

    args = {}
    if request.POST:
        archiveList = []

        postList, videoList, groupsList, photosList, infList = main()

        subTypeM = []

        subTypeM.append({
            'title': 'Видео',
            'value': videoList.count()
        })


        subTypeM.append({
            'title': 'Личная информация',
            'value': infList.count()
        })

        subTypeM.append({
            'title': 'Посты',
            'value': postList.count()
        })

        subTypeM.append({
            'title': 'Сообщества',
            'value': groupsList.count()
        })

        subTypeM.append({
            'title': 'Фото',
            'value': photosList.count()
        })

        archiveList.append({
            'title': 'Всего',
            'value': postList.count() + videoList.count() + groupsList.count() + photosList.count() + infList.count(),
            'subList': subTypeM
        })

        args = {
            'archiveList': archiveList
        }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

from threading import Thread

from django.db.models import Q

from Site.app.status.setStatus import setStatus
from Site.app.status.updateByAnalysis import updateByAnalysis
from Site.app.status.updateBySocial import updateBySocial
from Site.models import Social, CorruptInfo
from genering_profils_vk.src.func import *


def init(user=None):
    Thread(target=initT, args=[user]).start()


def initT(user=None):
    if user:
        socialList = Social.objects.filter(Q(controlUser=user) & Q(confirmedAt__isnull=False))
        for one in socialList.iterator():

            search_post_vk_id(one.value)
            print("Посты отработали")
            search_name_groups_vk_id(one.value)
            print("Группы отработали")
            search_name_videos_vk_id(one.value)
            print("Видео отработали")
            search_inf_users_vk_id(one.value)
            print("Информация отработали")
            # downloading_search_photos(one.value)
            # print("Фото отработали")
        else:
            print('NO initT')

        updateByAnalysis(user, 'robot')

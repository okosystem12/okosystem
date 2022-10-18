from threading import Thread

from django.db.models import Q

from Site.app.status.setStatus import setStatus
from Site.models import Social
from genering_profils_vk.src.func import *


def init(user=None):
    Thread(target=initT, args=[user]).start()


def initT(user=None):
    if user:
        socialList = Social.objects.filter(Q(controlUser=user))
        for one in socialList:
            print("start")
            abs_dir_path = os.path.abspath(os.path.join("verification_result"))
            abs_dir_path_user = os.path.join(abs_dir_path, str(one.value))
            if not os.path.exists(abs_dir_path_user):
                os.makedirs(abs_dir_path_user)

            res_post = search_post_vk_id(one.value, abs_dir_path_user)
            print("Посты\t", res_post)

            # res__name_groups = search_name_groups_vk_id(one.value, abs_dir_path_user)
            # print("Группы\t", res__name_groups)
            #
            # res_name_videos = search_name_videos_vk_id(one.value, abs_dir_path_user)
            # print("Видео\t", res_name_videos)
            #
            # res_inf_users = search_inf_users_vk_id(one.value, abs_dir_path_user)
            # print("Информация\t", res_inf_users)

            # res_search_photos = downloading_search_photos(one.value, abs_dir_path_user)
            # print("Фото\t", res_search_photos)
        else:
            print('NO initT')
        setStatus(user, 'warning' if socialList.count() else 'success')
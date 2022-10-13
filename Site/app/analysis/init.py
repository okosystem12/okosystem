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
            abs_dir_path = r"C:\Users\user.303-ARM2\PycharmProjects\okosystem\genering_profils_vk\verification_result"
            abs_dir_path_user = os.path.join(abs_dir_path, str(one.value))

            res_post = search_post_vk_id(one.value, abs_dir_path_user)
            print(res_post)

            res__name_groups = search_name_groups_vk_id(one.value, abs_dir_path_user)
            print(res__name_groups)

            res_name_videos = search_name_videos_vk_id(one.value, abs_dir_path_user)
            print(res_name_videos)

            res_inf_users = search_inf_users_vk_id(one.value, abs_dir_path_user)
            print(res_inf_users)

            res_search_photos = downloading_search_photos(one.value, abs_dir_path_user)
            print(res_search_photos)
        else:
            print('NO initT')
        setStatus(user, 'warning' if socialList.count() else 'success')

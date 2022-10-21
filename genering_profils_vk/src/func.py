#! /usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
import requests

from django.db.models import Q

from Site.models import Social, Post, Video, Groups, Inf, Photos, PostsChecks, PhotosChecks, GroupsChecks, VideoChecks, \
    AllUsersVK
from genering_profils_vk.src import config
from genering_profils_vk.src.evaluate import detect_photo

import asyncio
from aiohttp import ClientSession
import nest_asyncio
import json
import os
from time import sleep, time
try:
    from urllib import urlopen as urlopen
    from urllib import urlencode as urlencode
except ImportError:
    from urllib.request import urlopen as urlopen
    from urllib.parse import urlencode as urlencode

list_data = []

# ====================================================================СОЗДАНИЕ СЛОВАРЕЙ ДЛЯ БАЗЫ========================
# создание словаря для базы (ФОТО)
def create_dict_data(url, check_date, count_record, path_dir_photos, category, data):
    data[url] = {"check_date": check_date,
                 "inf_profile": {
                     "materials_profiles": {
                         "count_record": count_record,
                         "check_record": {
                             "path_dir_photos": path_dir_photos,
                             "category": category,
                         }
                     }
                 }
                 }


# создание словаря для базы (ПОСТЫ)
def create_dict_data_post(url_user, check_date, count_record, path_post, category, database):
    database[url_user] = {"check_date": check_date,
                          "inf_profile": {
                              "materials_profiles": {
                                  "count_record": count_record,
                                  "check_record": {
                                      "path_post": path_post,
                                      "category": category,
                                  }
                              }
                          }
                          }


# создание словаря для базы (НАЗВАНИЯ ГРУПП)
def create_dict_data_name_grops(url_user, check_date, count_record, path_groups, category, database):
    database[url_user] = {"check_date": check_date,
                          "inf_profile": {
                              "materials_profiles": {
                                  "count_record": count_record,
                                  "check_record": {
                                      "path_groups": path_groups,
                                      "category": category,
                                  }
                              }
                          }
                          }


# создание словаря для базы (НАЗВАНИЯ ВИДЕО)
def create_dict_data_name_videos(url_user, check_date, count_record, path_videos, category, database):
    database[url_user] = {"check_date": check_date,
                          "inf_profile": {
                              "materials_profiles": {
                                  "count_record": count_record,
                                  "check_record": {
                                      "path_videos": path_videos,
                                      "category": category,
                                  }
                              }
                          }
                          }


# создание словаря для базы (ИНФОРМАЦИЯ О ПОЛЬЗОВАТЕЛЕ)
def create_dict_data_inf_users(url_user, check_date, count_key_data, path_inf_user, category, database):
    database[url_user] = {"check_date": check_date,
                          "inf_profile": {
                              "materials_profiles": {
                                  "count_record": count_key_data,
                                  "check_record": {
                                      "path_videos": path_inf_user,
                                      "category": category,
                                  }
                              }
                          }
                          }


# создание каталога с датой и временем проверки
def create_dir_current_date_and_time(datetime):
    newpath = os.path.abspath(os.path.join("..", "verification_result", datetime))
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath


# ===========================================================================ПОИСК ПО КРИТЕРИЯМ=========================
# поиск по ключевым словам среди постов + {дата: имя}
def search_post_vk_id(owner_id, lst_dict=config.lst_dict, token=config.token):
    url = "https://api.vk.com/method/execute?"
    api = 'API.wall.get({"owner_id":"' + str(owner_id) + '", "count":"1"})'
    code = 'return [{'+api+'}];'
    data = dict(code=code, access_token=token, v='5.131')
    resp = requests.post(url=url, data=data)
    resp = resp.json()
    count_record = resp["response"][0]["count"]

    social = Social.objects.filter(Q(value=owner_id)).first()

    for i in range(count_record):
        url = "https://api.vk.com/method/execute?"
        api = 'API.wall.get({"owner_id":"' + str(owner_id) + '", "count":"1", "offset":"' + str(i) + '"})'
        code = 'return [{'+api+'}];'
        data = dict(code=code, access_token=token, v='5.131')
        resp = requests.post(url=url, data=data)
        resp = resp.json()
        try:
            for i_resp in range(len((resp["response"][0]["items"]))):
                post_list = PostsChecks.objects.filter(
                    Q(social=social)
                    & Q(id_post=resp["response"][0]["items"][i_resp]["id"])
                )
                if post_list.count() == 0:
                    PostsChecks.objects.create(
                        social=social,
                        id_post=resp["response"][0]["items"][i_resp]["id"]
                    )
                    for word_dict in lst_dict:
                        if word_dict.lower() in resp["response"][0]["items"][i_resp]["text"].lower():
                            Post.objects.create(
                                social=social,
                                id_post=resp["response"][0]["items"][i_resp]["id"],
                                date=datetime.utcfromtimestamp(resp["response"][0]["items"][i_resp]["date"]),
                                text=resp["response"][0]["items"][i_resp]["text"]
                            )
                            break
        except Exception as e:
            print(e)
            return


# скачивание всех фото пользователя + обработка + сохранение
def downloading_search_photos(user_id, token=config.token):

    def emoji_wipe(plain):
        array = bytearray(plain)
        while b'\xf0' in array:
            pos = array.find(b'\xf0')
            array = array.replace(array[pos:], array[pos + 4:])
        while b'\xe2' in array:
            pos = array.find(b'\xe2')
            array = array.replace(array[pos:], array[pos + 3:])
        return bytearray.decode(array, 'utf-8', errors='ignore')

    def request(method, params, is_one, return_data=True):
        try:
            sleep(request_interval)
            paramsWithVersion = params
            paramsWithVersion['v'] = '5.122'
            request_str = 'https://api.vk.com/method/%s?%s' % (method, urlencode(paramsWithVersion))
            r = urlopen(request_str).read()
            json_data = json.loads(emoji_wipe(r))
            if 'error' in json_data:
                return {'error': json_data['error']}
            if 'response' in json_data:
                json_data = json_data['response']
                if return_data:
                    if 'items' in json_data:
                        json_data = json_data['items']
                    json_data = list(json_data)
                    if is_one == True:
                        return json_data.pop()
                    else:
                        return json_data
                else:
                    return json_data['count']
            if not 'error' in json_data and not 'response' in json_data:
                return {'error': 'unknown error'}
        except Exception:
            pass

    photo_type_sort_arr = ['w', 'z', 'y', 'x', 'r', 'q', 'p', 'o', 'm', 's']


    def extract_pirture_url(response):
        try:
            sizes = response['sizes']
            sizes_sorted = sorted(sizes, key=lambda size: photo_type_sort_arr.index(str(size['type'])))
            size_selected = sizes_sorted[0]
            url = str(size_selected['url']).replace(" ", "")
            return url
        except:
            return '???'

    def get_photos_album(uid, token, file_name, album_id, social):
        req_count = 200
        params = {}
        params['access_token'] = token
        params['owner_id'] = uid
        params['count'] = 0
        params['album_id'] = str(album_id)
        photos_count = request('photos.get', params, is_one=True, return_data=False)
        path = file_name
        if photos_count:
            try:
                fave_iterations = int(photos_count / req_count) + 1
                params['count'] = req_count
                for i in range(0, fave_iterations, 1):
                    params['offset'] = req_count * i
                    photos_response = request('photos.get', params, is_one=False)
                    for each in photos_response:
                        if each != 'error':
                            try:
                                link = extract_pirture_url(each) # получили ссылку на фото Todo

                                photos_list = PhotosChecks.objects.filter(
                                    Q(social=social)
                                    & Q(link=link)
                                )

                                if photos_list.count() == 0:
                                    PhotosChecks.objects.create(
                                        social=social,
                                        link=link
                                    )
                                    with open(path, 'a') as f:
                                        f.write('%s\n' % link)
                            except Exception as e:
                                pass
            except Exception as e:
                pass
        else:
            pass

    def get_photos(uid, token, directory_name, social):
        album_ids = [-6, -7, -15]
        delim = ';'  # TODO ??
        uid_list = []
        if delim not in uid:
            uid_list.append(uid)
        else:
            uids_b = uid.split(delim)
            for i in range(int(uids_b[0]), int(uids_b[1]) + 1):
                uid_list.append(i)

        for uid_line in uid_list:
            for index, album_num in enumerate(album_ids):
                get_photos_album(uid_line, token, directory_name, album_num, social)

    request_interval = 0

    # создание каталога для фоток в каталоге с id пользователя
    dir_for_photos_tmp = os.path.abspath("tmp")
    if not os.path.exists(dir_for_photos_tmp):
        os.makedirs(dir_for_photos_tmp)

    # создание файла со ссылками в этом каталоге
    file_with_photos = os.path.abspath(os.path.join("tmp", '%s.txt' % 'photos_user_' +str(user_id)))

    social = Social.objects.filter(Q(value=user_id)).first()

    # получение ссылок на фото
    get_photos(user_id, token, file_with_photos, social)
    if os.path.exists(file_with_photos):
        f = open(file_with_photos, 'r')
        photos_txt = f.read()
        f.close()
    else:
        os.rmdir(dir_for_photos_tmp)
        return
    os.remove(file_with_photos)
    links = photos_txt.split('\n')
    links = links[:-1]

    # скачивание фото
    for number, link in enumerate(links):
        try:
            url_as = link
            file_name = str(number + 1) + ".jpg"
            file_name_abs = os.path.join(dir_for_photos_tmp, file_name)
            if not os.path.isfile(file_name_abs):
                resource = urlopen(url_as)
                out = open(file_name_abs, 'wb')
                out.write(resource.read())
                out.close()

                # проверка нейронкой
                if detect_photo(model, file_name_abs):
                    Photos.objects.create(
                        social=social,
                        link=link
                    )
                os.remove(file_name_abs)
        except Exception:
            pass

    os.rmdir(dir_for_photos_tmp)
    return


# поиск по ключевым словам среди списка сообществ
def search_name_groups_vk_id(user_id, lst_dict=config.lst_dict, token=config.token):
    url = "https://api.vk.com/method/execute?"
    api = 'API.groups.get({"user_id":"' + str(user_id) + '", "count":"1"})'
    code = 'return [{'+api+'}];'
    data = dict(code=code, access_token=token, v='5.131')
    resp = requests.post(url=url, data=data)
    resp = resp.json()
    count_record = resp["response"][0]["count"]

    social = Social.objects.filter(Q(value=user_id)).first()

    for i in range(count_record):
        url = "https://api.vk.com/method/execute?"
        api = 'API.groups.get({"user_id":"' + str(user_id) + '", "count":"1", "extended":"1", "offset":"' + str(
            i) + '"})'
        code ='return [{'+api+'}];'
        data = dict(code=code, access_token=token, v='5.131')
        resp = requests.post(url=url, data=data)
        resp = resp.json()

        try:
            for i_resp in range(len((resp["response"][0]["items"]))):
                groups_list = GroupsChecks.objects.filter(
                    Q(social=social)
                    & Q(id_groups=resp["response"][0]["items"][0]["id"])
                )
                if groups_list.count() == 0:
                    GroupsChecks.objects.create(
                        social=social,
                        id_groups=resp["response"][0]["items"][0]["id"]
                    )
                    for word_dict in lst_dict:
                        if word_dict.lower() in resp["response"][0]["items"][i_resp]["name"].lower():
                            Groups.objects.create(
                                social=social,
                                id_groups=int(resp["response"][0]["items"][i_resp]["id"]),
                                name=resp["response"][0]["items"][i_resp]["name"]
                            )

                            break
        except Exception:
            return


# поиск по ключевым словами среди списка видеозаписей + {дата: имя}
def search_name_videos_vk_id(owner_id, lst_dict=config.lst_dict, token=config.token):
    url = "https://api.vk.com/method/execute?"
    api = 'API.video.get({"user_id":"' + str(owner_id) + '", "count":"1"})'
    code = 'return [{'+api+'}];'
    data = dict(code=code, access_token=token, v='5.131')
    resp = requests.post(url=url, data=data)
    resp = resp.json()
    count_record = resp["response"][0]["count"]

    social = Social.objects.filter(Q(value=owner_id)).first()

    for i in range(count_record):
        url = "https://api.vk.com/method/execute?"
        api = 'API.video.get({"user_id":"' + str(owner_id) + '", "count":"1", "extended":"1", "offset":"' + str(
            i) + '"})'
        code = 'return [{'+api+'}];'
        data = dict(code=code, access_token=token, v='5.131')
        resp = requests.post(url=url, data=data)
        resp = resp.json()

        try:
            for i_resp in range(len((resp["response"][0]["items"]))):
                video_list = VideoChecks.objects.filter(
                    Q(social=social)
                    & Q(id_video=resp["response"][0]["items"][i_resp]["id"])
                )
                if video_list.count() == 0:
                    VideoChecks.objects.create(
                        social=social,
                        id_video=resp["response"][0]["items"][i_resp]["id"]
                    )
                    for word_dict in lst_dict:
                        if word_dict.lower() in resp["response"][0]["items"][0]["title"].lower():
                            Video.objects.create(
                                social=social,
                                id_video=int(resp["response"][0]["items"][0]["id"]),
                                date=datetime.utcfromtimestamp(resp["response"][0]["items"][0]["date"]),
                                name=resp["response"][0]["items"][0]["title"],
                                link=resp["response"][0]["items"][0]["player"]
                            )
                            break
        except Exception as e:
            print(e)
            return


# поиск по всей указанной информации о пользователе
def search_inf_users_vk_id(owner_id, lst_dict=config.lst_dict, token=config.token):
    url = "https://api.vk.com/method/execute?"
    api = 'API.users.get({"user_ids":"' + str(
        owner_id) + '", "fields": "id, about, activities, books, games, interests, movies, music, nickname, quotes, status, tv"})'
    code = 'return [{'+api+'}];'
    data = dict(code=code, access_token=token, v='5.131')
    resp = requests.post(url=url, data=data)
    resp = resp.json()
    data = {
        "О себе": resp.get("response")[0][0].get("about", None),
        "Деятельность": resp.get("response")[0][0].get("activities", None),
        "Любимые книги": resp.get("response")[0][0].get("books", None),
        "Любимые игры": resp.get("response")[0][0].get("games", None),
        "Интересы": resp.get("response")[0][0].get("interests", None),
        "Любимые фильмы": resp.get("response")[0][0].get("movies", None),
        "Любимая музыка": resp.get("response")[0][0].get("music", None),
        "Никнейм": resp.get("response")[0][0].get("nickname", None),
        "Любимые цитаты": resp.get("response")[0][0].get("quotes", None),
        "Статус пользователя": resp.get("response")[0][0].get("status", None),
        "Любимые телешоу": resp.get("response")[0][0].get("tv", None)
    }

    social = Social.objects.filter(Q(value=owner_id)).first()

    if not data:
        return
    else:
        try:
            for key, value in data.items():
                for word in lst_dict:
                    if str(word.lower()) in str(value.lower()):
                        Inf.objects.create(
                            social=social,
                            about=data["О себе"],
                            activities=data["Деятельность"],
                            books=data["Любимые книги"],
                            games=data["Любимые игры"],
                            interests=data["Интересы"],
                            movies=data["Любимые фильмы"],
                            music=data["Любимая музыка"],
                            nickname=data["Никнейм"],
                            quotes=data["Любимые цитаты"],
                            status=data["Статус пользователя"],
                            tv=data["Любимые телешоу"]
                        )
                        return
        except Exception as e:
            print(e)
            return


# обновление базы пользователей
# доделать вывод в базу, а не в файл!!! todo
# id_user_last = AllUsersVK.objects.order_by("id_user").last()
def update_inf_users(list_token, id_user_last):
    nest_asyncio.apply()

    async def bound_fetch_zero(sem, id, session):
        async with sem:
            await fetch_zero(id, session)

    async def fetch_zero(id, session):
        url = build_url(id)
        try:
            async with session.get(url) as response:
                # Считываем json
                resp = await response.text()
                js = json.loads(resp)
                for it in range(25):
                    list_data.append(js["response"][it][0])

        except Exception as ex:
            print(resp)
            return

    def build_url(id):
        api = "API.users.get({{'user_ids':{},'fields':'deactivated, is_closed, first_name, last_name, bdate, city, home_town'}})".format(
            id * 25 + 1)
        for i in range(2, 26):
            api += ",API.users.get({{'user_ids':{},'fields':'deactivated, is_closed, first_name, last_name, bdate, city, home_town'}})".format(
                id * 25 + i)
        url = 'https://api.vk.com/method/execute?access_token={}&v=5.101&code=return%20[{}];'.format(
            list_token[id % len(list_token)], api)
        return url

    async def run_zero(id):
        tasks = []
        sem = asyncio.Semaphore(1000)

        async with ClientSession() as session:
            #  Значение 3200 зависит от вашего числа токенов
            param3200 = 320
            for id in range((id - 1) * param3200, id * param3200):
                task = asyncio.ensure_future(bound_fetch_zero(sem, id, session))
                tasks.append(task)

            responses = asyncio.gather(*tasks)
            await responses
            del responses
            await session.close()


    # Запускаем  сборщик
    # threshold = 17
    # param_count = 554
    st = time()
    # 105 and 900
    all = 320*25*900
    threshold = id_user_last // all
    for i in range(threshold, threshold + 3):
        param_count = 900
        for query in range(i * param_count + 1, (i + 1) * param_count + 1):
            string = json.dumps(list_data)
            with open(os.path.join("database", f"database-VK-users_{query}.txt"), "a", encoding="utf-8") as file:
                file.write(string + "\n")
            list_data.clear()
            print(query, time()-st)
            st = time()
            loop = asyncio.get_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(run_zero(query))


# полное заполнение базы данных ВК
def read_files_for_bd(path_dir):

    # AllUsersVK.objects.all().delete()
    # return

    for namefile in os.listdir(path_dir):
        with open(os.path.join(path_dir, namefile), "r", encoding="utf-8") as file:
            data = [json.loads(line) for line in file]

        data_update = [elem for l in data for elem in l if
                       elem.get("deactivated") not in ("deleted", "banned") and not elem.get("is_closed")]
        for l in data_update:
            bdate = l.get("bdate", "")
            city = l.get("city", "")
            if isinstance(city, dict):
                city = city.get("title")

            # вап
            AllUsersVK.objects.create(
                id_user=l.get("id", ""),
                first_name=l.get("first_name", ""),
                last_name=l.get("last_name", ""),
                bdate=bdate,
                home_town=l.get("home_town", ""),
                city=city
            )
        data.clear()
        data_update.clear()

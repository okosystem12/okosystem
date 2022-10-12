#! /usr/bin/python
# -*- coding: utf-8 -*-
import asyncio
from aiohttp import ClientSession
import nest_asyncio
from time import time
import vk_api
from pprint import pprint
import os
import requests
import json
from genering_profils_vk.src.func import *
import sys
import json
import os
from shutil import rmtree
from time import sleep, time
from genering_profils_vk.src import config
from datetime import datetime
try:
    from urllib import urlopen as urlopen
    from urllib import urlencode as urlencode
except ImportError:
    from urllib.request import urlopen as urlopen
    from urllib.parse import urlencode as urlencode

list_data = []

# глобальные переменные ддя словаря (общее кол-во фото и путь до директории с фото)
count_photo_global = 0
path_dir_photos_global = ""

# глобальные переменные ддя словаря (общее кол-во ПОСТОВ и путь до файла с найденными постами)
count_text_global = 0
path_file_text_global = ""

# глобальные переменные ддя словаря (общее кол-во ГРУПП и путь до файла с найденными названиями групп)
count_text_groups_global = 0
path_file_text_groups_global = ""

# глобальные переменные ддя словаря (общее кол-во ВИДЕО и путь до файла с найденными названиями ВИДЕО)
count_video_global = 0
path_file_video_global = ""

# глобальные переменные для словаря (общее кол-во НАЙДЕННЫХ ЗАПИСЕЙ В СЛОВАРЕ и путь до файла с найденными ЗАПИСЯМИ)
count_key_data_global = 0
path_file_inf_users_global = ""


# ====================================================================СОЗДАНИЕ СЛОВАРЕЙ ДЛЯ БАЗЫ========================
# создание словаря для базы (ФОТО)
def create_dict_data(url, check_date, count_record, path_dir_photos, category, data):
    data[url] ={"check_date": check_date,
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
def search_post_vk_id(owner_id, abs_dir_path_user, lst_dict=config.lst_dict, token=config.token):
    url = "https://api.vk.com/method/execute?"
    api = 'API.wall.get({"owner_id":"' + str(owner_id) + '", "count":"1"})'
    code = f'return [{api}];'
    data = dict(code=code, access_token=token, v='5.131')
    resp = requests.post(url=url, data=data)
    resp = resp.json()
    count_record = resp["response"][0]["count"]
    global count_text_global
    count_text_global = count_record
    global path_file_text_global
    path_file_text_global = os.path.join(abs_dir_path_user, f"post_user_{owner_id}.txt")


    for i in range(count_record):
        url = "https://api.vk.com/method/execute?"
        api = 'API.wall.get({"owner_id":"' + str(owner_id) + '", "count":"1", "offset":"' + str(i) + '"})'
        code = f'return [{api}];'
        data = dict(code=code, access_token=token, v='5.131')
        resp = requests.post(url=url, data=data)
        resp = resp.json()

        try:
            for i_resp in range(len((resp["response"][0]["items"]))):
                for word_dict in lst_dict:
                    if word_dict.lower() in resp["response"][0]["items"][i_resp]["text"].lower():
                        with open(os.path.join(abs_dir_path_user, f"post_user_{owner_id}.txt"), "a", encoding="utf-8") as file:
                            dt = (resp["response"][0]["items"][i_resp]["date"])
                            file.write(datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S') + ": " + resp["response"][0]["items"][i_resp]["text"] + "\n" + "=" * 1000 + "\n")
                        break
        except Exception:
            break


# скачивание всех фото пользователя + обработка + сохранение
def downloading_search_photos(user_id, dir_path_date_and_time, token=config.token):
    def touch(path):
        with open(path, 'a'):
            os.utime(path, None)

    # создание файла со сслыками на фото
    def create_file(file_path, deleteIfExists):
        if os.path.exists(file_path):
            if deleteIfExists:
                os.remove(file_path)
                touch(file_path)
        else:
            touch(file_path)

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

    def get_photos_method(uid, token, file_name, photo_method):
        req_count = 200
        params = {}
        params['access_token'] = token
        params['owner_id'] = uid
        params['count'] = 0
        photos_count = request('photos.%s' % photo_method, params, is_one=True, return_data=False)
        global count_photo_global
        count_photo_global = photos_count
        path = file_name
        if photos_count:
            try:
                f = open(path, 'a')
                fave_iterations = int(photos_count / req_count) + 1
                params['count'] = req_count
                for i in range(0, fave_iterations, 1):
                    params['offset'] = req_count * i
                    photos_response = request('photos.%s' % photo_method, params, is_one=False)
                    for each in photos_response:
                        link = extract_pirture_url(each)
                        f.write('%s:%s\n' % (str(uid), link))
                f.close()
            except Exception:
                pass
        else:
            pass

    def get_photos_album(uid, token, file_name, album_id):
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
                f = open(path, 'a')
                fave_iterations = int(photos_count / req_count) + 1
                params['count'] = req_count
                for i in range(0, fave_iterations, 1):
                    params['offset'] = req_count * i
                    photos_response = request('photos.get', params, is_one=False)
                    for each in photos_response:
                        if each != 'error':
                            try:
                                link = extract_pirture_url(each)
                                f.write('%s:%s\n' % (str(uid), link))
                            except Exception:
                                pass
                f.close()
            except Exception:
                pass
        else:
            pass

    def get_photos(uid, token, directory_name):
        download_methods = ['getAll']  # , 'getUserPhotos' 'getNewTags'
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
            for index, d_method in enumerate(download_methods):
                get_photos_method(uid_line, token, directory_name, d_method)
            for index, album_num in enumerate(album_ids):
                get_photos_album(uid_line, token, directory_name, album_num)

    request_interval = 0
    file_with_token = 'token'

    # создание каталога с id пользователя
    path_user_id = os.path.abspath(os.path.join(dir_path_date_and_time, str(user_id)))
    if not os.path.exists(path_user_id):
        os.makedirs(path_user_id)

    # создание файла со ссылками в этом каталоге
    file_with_photos = os.path.abspath(os.path.join(path_user_id, '%s.txt' % f"photos_user_{str(user_id)}"))
    create_file(file_with_photos, True)

    # создание каталога для фоток в каталоге с id пользователя
    path_photos = os.path.abspath(os.path.join(path_user_id, "photos"))
    global path_dir_photos_global
    path_dir_photos_global = path_photos
    if not os.path.exists(path_photos):
        os.makedirs(path_photos)

    # получение ссылок на фото
    get_photos(user_id, token, file_with_photos)
    f = open(file_with_photos, 'r')
    photos_txt = f.read()
    f.close()
    links = photos_txt.split('\n')
    links = links[:-1]
    total = len(links)

    # скачивание фото
    for number, link in enumerate(links):
        try:
            url_as = link[link.find(':') + 1:]
            file_name = str(number+1) + ".jpg"
            file_name_abs = os.path.join(path_photos, file_name)
            if not os.path.isfile(file_name_abs):
                resource = urlopen(url_as)
                out = open(file_name_abs, 'wb')
                # ============================================================================
                #     сюда проверку модели нейронки (полный путь до фото file_name_abs
                #       потом удаляем сразу, если не нашли
                # =============================================================================
                #print(file_name_abs)
                out.write(resource.read())
                out.close()
        except Exception:
            pass

    # если нет фото (или страница закрыта) удаляем каталог и файл со ссылками
    if not os.listdir(path_photos):
        os.rmdir(path_photos)
        os.remove(file_with_photos)
        os.rmdir(path_user_id)


# поиск по ключевым словам среди списка сообществ
def search_name_groups_vk_id(user_id, abs_dir_path_user, lst_dict=config.lst_dict, token=config.token):
    url = "https://api.vk.com/method/execute?"
    api = 'API.groups.get({"user_id":"' + str(user_id) + '", "count":"1"})'
    code = f'return [{api}];'
    data = dict(code=code, access_token=token, v='5.131')
    resp = requests.post(url=url, data=data)
    resp = resp.json()
    count_record = resp["response"][0]["count"]
    global count_text_groups_global
    count_text_groups_global = count_record
    global path_file_text_groups_global
    path_file_text_groups_global = os.path.join(abs_dir_path_user, f"groups_user_{user_id}.txt")

    for i in range(count_record):
        url = "https://api.vk.com/method/execute?"
        api = 'API.groups.get({"user_id":"' + str(user_id) + '", "count":"1", "extended":"1", "offset":"' + str(
            i) + '"})'
        code = f'return [{api}];'
        data = dict(code=code, access_token=token, v='5.131')
        resp = requests.post(url=url, data=data)
        resp = resp.json()

        try:
            for i_resp in range(len((resp["response"][0]["items"]))):
                for word_dict in lst_dict:
                    if word_dict.lower() in resp["response"][0]["items"][i_resp]["name"].lower():
                        with open(os.path.join(abs_dir_path_user, f"groups_user_{user_id}.txt"), "a",
                                  encoding="utf-8") as file:
                            file.write(resp["response"][0]["items"][i_resp]["name"] + "\n" + "=" * 1000 + "\n")
                        break
        except Exception:
            pass


# поиск по ключевым словами среди списка видеозаписей + {дата: имя}
def search_name_videos_vk_id(owner_id, abs_dir_path_user, lst_dict=config.lst_dict, token=config.token):
    url = "https://api.vk.com/method/execute?"
    api = 'API.video.get({"user_id":"' + str(owner_id) + '", "count":"1"})'
    code = f'return [{api}];'
    data = dict(code=code, access_token=token, v='5.131')
    resp = requests.post(url=url, data=data)
    resp = resp.json()
    count_record = resp["response"][0]["count"]
    global count_video_global
    count_video_global = count_record
    global path_file_video_global
    path_file_video_global = os.path.join(abs_dir_path_user, f"videos_user_{owner_id}.txt")

    for i in range(count_record):
        url = "https://api.vk.com/method/execute?"
        api = 'API.video.get({"user_id":"' + str(owner_id) + '", "count":"1", "extended":"1", "offset":"' + str(i) + '"})'
        code = f'return [{api}];'
        data = dict(code=code, access_token=token, v='5.131')
        resp = requests.post(url=url, data=data)
        resp = resp.json()

        try:
            for i_resp in range(len((resp["response"][0]["items"]))):
                for word_dict in lst_dict:
                    if word_dict.lower() in resp["response"][0]["items"][0]["title"].lower():
                        with open(os.path.join(abs_dir_path_user, f"videos_user_{owner_id}.txt"), "a", encoding="utf-8") as file:
                            dt = (resp["response"][0]["items"][0]["date"])
                            file.write(datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S') + ": " + resp["response"][0]["items"][0]["title"] + "\n" + "=" * 1000 + "\n")
                        break
        except Exception:
            pass


# поиск по всей указанной информации о пользователе
def search_inf_users_vk_id(owner_id, abs_dir_path_user, lst_dict=config.lst_dict, token=config.token):
    global path_file_inf_users_global
    global count_key_data_global
    url = "https://api.vk.com/method/execute?"
    api = 'API.users.get({"user_ids":"' + str(owner_id) + '", "fields": "about, activities, books, games, interests, movies, music, nickname, quotes, status, tv"})'
    code = f'return [{api}];'
    data = dict(code=code, access_token=token, v='5.131')
    resp = requests.post(url=url, data=data)
    resp = resp.json()
    data = {
        "О себе": resp.get("response")[0][0].get("about", False),
        "Деятельность": resp.get("response")[0][0].get("activities", False),
        "Любимые книги": resp.get("response")[0][0].get("books", False),
        "Любимые игры": resp.get("response")[0][0].get("games", False),
        "Интересы": resp.get("response")[0][0].get("interests", False),
        "Любимые фильмы": resp.get("response")[0][0].get("movies", False),
        "Любимая музыка": resp.get("response")[0][0].get("music", False),
        "Никнейм ": resp.get("response")[0][0].get("nickname", False),
        "Любимые цитаты": resp.get("response")[0][0].get("quotes", False),
        "Статус пользователя": resp.get("response")[0][0].get("status", False),
        "Любимые телешоу": resp.get("response")[0][0].get("tv", False)
    }

    for key, value in list(data.items()):
        if not value:
            del data[key]

    if not data:
        path_file_inf_users_global = ""
        count_key_data_global  = 0
        return
    else:
        path_file_inf_users_global = os.path.join(abs_dir_path_user, f"inf_user_{owner_id}.txt")
        count_key_data_global = len(data.keys())
        try:
            for key, value in data.items():
                for word in lst_dict:
                    if word.lower() in value.lower():
                        with open(os.path.join(abs_dir_path_user, f"inf_user_{owner_id}.txt"), "a",
                                  encoding="utf-8") as file:
                            file.write(key + ": " + value + "\n" + "=" * 1000 + "\n")

        except Exception:
            pass
# ====================================================================ОБОБЩАЮЩАЯ ФУНКЦИЯ================================
# пробег по всем пользователям вк c использованием поиска фото, постов
def collector(list_token, dir_path_date_and_time, dt):
    nest_asyncio.apply()
    data_photos = {}
    data_posts = {}
    data_groups = {}
    data_videos = {}
    data_inf_users = {}

    async def bound_fetch_zero(sem, id, session):
        async with sem:
            await fetch_zero(id, session)

    #ЗДЕСЬ ДОБАВЛЯЕМ ПОИСК ПО ФОТО И ВСЁ ОСТАЛЬНОЕ
    async def fetch_zero(id, session):
        url = build_url(id)
        try:
            async with session.get(url) as response:
                # Считываем json
                resp = await response.text()
                js = json.loads(resp)
                list_users = [x for x in js['response'] if x != False]

                # Проверяем если город=1(Москва) тогда добавляем в лист
                for it in list_users:
                    list_data.append(it[0]['id'])
                    try:
                        # если город Москва
                        # if it[0]['city']['id'] == 1 and it[0]['id'] == 18:
                        if it[0]['id'] == 23:
                            # ДОБАВЛЕНИЕ В СПИСОК ID СТРАНИЦЫ (ЗДЕСЬ НАЧИНАЕМ ПРОВЕРЯТЬ ИНФОРМАЦИЮ) TODO

                            # выкачивание фото
                            # downloading_search_photos(str(it[0]['id']), dir_path_date_and_time)

                            dir_id_path = os.path.join(dir_path_date_and_time, str(it[0]['id']))
                            if not os.path.exists(dir_id_path):
                                os.makedirs(dir_id_path)

                            # выкачивание и проверка постов
                            search_post_vk_id(it[0]['id'], dir_id_path)

                            # выкачивание и проверка названий групп и сообществ
                            search_name_groups_vk_id(it[0]['id'], dir_id_path)

                            # выкачивание и проверка названий видеозаписей
                            search_name_videos_vk_id(it[0]['id'], dir_id_path)

                            # выкачивание и провекра всей информации о пользователе
                            search_inf_users_vk_id(it[0]['id'], dir_id_path)

                            # если каталог пуст, удаляем
                            if not os.listdir(dir_id_path):
                                os.rmdir(dir_id_path)



                            # инфомация для заполненеия базы
                            url = f"https://vk.com/id{it[0]['id']}"
                            check_date = dt
                            count_record = count_photo_global
                            path_dir_photos = path_dir_photos_global
                            category = "Раскрытие принадлежности к центральному аппарату МО РФ"

                            create_dict_data(url, check_date, count_record, path_dir_photos, category, data_photos)
                            create_dict_data_post(url, check_date, count_text_global, path_file_text_global, "Новая категория (ПОСТЫ)", data_posts)
                            create_dict_data_name_grops(url, check_date, count_text_groups_global, path_file_text_groups_global, "Новая категория (ГРУППЫ)", data_groups)
                            create_dict_data_name_videos(url, check_date, count_video_global, path_file_video_global, "Категория ВИДЕО", data_videos)
                            create_dict_data_inf_users(url, check_date, count_key_data_global, path_file_inf_users_global, "Категория ИНФОРМАЦИЯ О ПОЛЬЗОВАТЕЛЯХ", data_inf_users)


                    except Exception:
                        pass
        except Exception as ex:
            print(resp)

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
            param3200 = 250000
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
    threshold = 3
    for i in range(threshold):
        param_count = 40
        for query in range(i * param_count + 1, (i + 1) * param_count + 1):
            print(query, time()-st)
            st = time()
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(run_zero(query))

    print(len(list_data))

    return {"photos":data_photos,
            "posts":data_posts,
            "groups":data_groups,
            "videos":data_videos,
            "inf_user":data_inf_users}

import json
import os
import django
import datetime


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.apps import AppConfig

from Site.models import AllUsersVK


def read_files_for_bd(path_dir):

    AllUsersVK.objects.all().delete()
    return

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

read_files_for_bd(os.path.abspath(os.path.join("..", "database")))
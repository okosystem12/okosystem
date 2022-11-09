import json

import requests

from Site.app.object.elem import elem


def inflect(string=''):
    try:
        r = requests.get('https://htmlweb.ru/json/service/inflect?inflect=' + string)

        if r.status_code == 200:
            rList = json.loads(r.text)
            return elem(rList, 'items', [])
    except Exception as e:
        print(e)
    return [string]

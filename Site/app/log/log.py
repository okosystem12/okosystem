import json
from datetime import datetime

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.models import Logs


def log(user=None, place='', action='', details='', description={}):
    Logs.objects.create(user_id=user, place=place,
                        action=action, details=details,
                        description=json.dumps(description, default=my_convert_datetime),
                        date=datetime.now())

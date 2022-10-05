from datetime import datetime, date
from threading import Thread
import time

from django.db.models import Q

from Site.apps.queue import que
from Site.models import LastUpdateConfig


def logUpdateThread():
    que.add_element(Thread(target=logUpdate, args=[LastUpdateConfig]))


def logUpdate():
    LastUpdateConfig.objects.create(
        type='vkLastUpdateDate',
        dateStart=datetime.now()
    )

    time.sleep(10)

    lastUpdate = LastUpdateConfig.objects.filter(Q(type='vkLastUpdateDate')).order_by('-dateStart').first()

    if lastUpdate.dateEnd is None:
        lastUpdate.dateEnd = datetime.now()
        lastUpdate.save()
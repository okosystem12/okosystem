import time
from datetime import datetime
from threading import Thread

from Site.app.queue import que
from Site.models import LastUpdateConfig


def logUpdate():
    que.add_element(Thread(target=logUpdateThread, args=[]))


def logUpdateThread():
    LastUpdateConfig.objects.create(
        type='vkLastUpdateDate',
        dateStart=datetime.now()
    )

    time.sleep(10)

    lastUpdate = LastUpdateConfig.objects.filter(Q(type='vkLastUpdateDate')).order_by('-dateStart').first()

    if lastUpdate.dateEnd is None:
        lastUpdate.dateEnd = datetime.now()
        lastUpdate.save()

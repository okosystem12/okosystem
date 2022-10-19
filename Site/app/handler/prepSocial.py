from django.db.models import Q

from Site.models import Social


def prepSocial(user=None):
    result = []

    for one in Social.objects.filter(Q(controlUser=user) & Q(confirmedAt__isnull=False)):
        result.append({
            'href': one.prefix + one.value
        })

    return result

from django.db.models import Q

from Site.models import Countries, Regions, Cities


def place(_type=''):
    countriesList = Countries.objects.filter(Q(removeAt=None))
    regionsList = Regions.objects.filter(Q(removeAt=None) & Q(country__in=countriesList))
    citiesList = Cities.objects.filter(Q(removeAt=None) & (Q(region__in=regionsList) | Q(country__in=countriesList)))

    if _type == 'countries':
        regionsList = regionsList.filter(Q(pk=None))
        citiesList = citiesList.filter(Q(pk=None))
    elif _type == 'regions':
        citiesList = citiesList.filter(Q(pk=None))

    return countriesList, regionsList, citiesList

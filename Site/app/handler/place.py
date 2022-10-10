from django.db.models import Q

from Site.models import Countries, Regions, Cities


def placeObject(_type=''):
    regionsList = []
    citiesList = []

    countriesList = Countries.objects.filter(Q(removeAt=None))

    if _type == '':
        regionsList = Regions.objects.filter(Q(removeAt=None) & Q(country__in=countriesList))
        citiesList = Cities.objects.filter(
            Q(removeAt=None) & (Q(region__in=regionsList) | Q(country__in=countriesList)))

        regionsList = list(regionsList.values())
        citiesList = list(citiesList.values())
    elif _type == 'regions':
        regionsList = Regions.objects.filter(Q(removeAt=None) & Q(country__in=countriesList))

        regionsList = list(regionsList.values())

    return {
        'countriesList': list(countriesList.values()),
        'regionsList': regionsList,
        'citiesList': citiesList,
    }

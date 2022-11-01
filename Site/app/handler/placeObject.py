
from Site.app.handler.place import place


def placeObject(_type=''):
    countriesList, regionsList, citiesList = place(_type)

    return {
        'countriesList': list(countriesList.values()),
        'regionsList': list(regionsList.values()),
        'citiesList': list(citiesList.values()),
    }

from Site.models import Countries, Regions, Cities


def placeDisassemble(place=None):
    result = []
    if place:
        country = Countries.objects.filter(pk=place.country_id).first()
        region = Regions.objects.filter(pk=place.region_id).first()
        city = Cities.objects.filter(pk=place.city_id).first()

        result.append(country.title if country else None)
        result.append(region.title if region else None)
        result.append(city.title if city else None)

    return result

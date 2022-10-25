def prepInfo(countriesList, regionsList, citiesList):
    emptyRow = {'id': '', 'country': '', 'region': '', 'city': ''}
    index = 0
    result = []

    regionPrefix = countriesList.count() + 1000
    cityPrefix = regionPrefix + regionsList.count() + 1000

    for country in countriesList:
        info = {}
        info.update(emptyRow)
        info.update({'id': index, 'typeRow': 'country', 'realId': country.id, 'country': country.title})
        result.append(info)
        index += 1

    for region in regionsList:
        info = {}
        info.update(emptyRow)
        info.update({'id': regionPrefix + index, 'typeRow': 'region', 'realId': region.id, 'region': region.title,
                     'country': region.country.title, 'country_id': region.country.id})

        result.append(info)
        index += 1

    for city in citiesList:
        info = {}
        info.update(emptyRow)
        info.update({'id': cityPrefix + index, 'typeRow': 'city', 'realId': city.id, 'city': city.title,
                     'country': city.country.title, 'country_id': city.country.id,
                     'region': city.region.title if city.region else '',
                     'region_id': city.region.id if city.region else ''})

        result.append(info)
        index += 1

    return result

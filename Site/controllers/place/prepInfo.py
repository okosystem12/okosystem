def prepInfo(countriesList, regionsList, citiesList):
    emptyRow = {'id': '', 'country': '', 'region': '', 'city': ''}
    index = 0
    result = []

    for country in countriesList.iterator():
        info = {}
        info.update(emptyRow)
        info.update({'id': index, 'typeRow': 'country', 'realId': country.id, 'country': country.title})
        result.append(info)
        index += 1

    index += 1000

    for region in regionsList.iterator():
        info = {}
        info.update(emptyRow)
        info.update({'id': index, 'typeRow': 'region', 'realId': region.id, 'region': region.title,
                     'country': region.country.title, 'country_id': region.country.id})

        result.append(info)
        index += 1

    index += 1000

    for city in citiesList.iterator():
        info = {}
        info.update(emptyRow)
        info.update({'id': index, 'typeRow': 'city', 'realId': city.id, 'city': city.title,
                     'country': city.country.title, 'country_id': city.country.id,
                     'region': city.region.title if city.region else '',
                     'region_id': city.region.id if city.region else ''})

        result.append(info)
        index += 1

    return result

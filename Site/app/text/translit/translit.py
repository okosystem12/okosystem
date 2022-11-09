from Site.app.text.translit.translitDict import translitDict


def translit(string=''):
    result = ''

    dList = translitDict()
    keyList = list(dList.keys())

    for l in string:
        if l in keyList:
            result += dList[l]
        else:
            result += l

    return result

from Site.app.text.translit.translitDict import translitDict


def replPart(string='', dList={}):
    string = string.lower()
    result = [string]

    keyList = list(dList.keys())

    posList = []

    for key in keyList:
        if key in string:
            posList += [i for i, letter in enumerate(string) if letter == key]

    for pos in posList:
        strBuf = string[:pos] + dList[string[pos]] + string[pos+1:]
        result.append(strBuf)
        result += replPart(strBuf, dList)

    return list(set(result))

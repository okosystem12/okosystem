def replFull(string='', dList={}):
    result = ''
    keyList = list(dList.keys())

    for l in string:
        if l in keyList:
            result += dList[l]
        else:
            result += l

    return result

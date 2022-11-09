from Site.app.text.alter.alterPart import alterPart
from Site.app.text.decim.decimPart import decimPart
from Site.app.text.inflect import inflect
from Site.app.text.mimic.mimicPart import mimicPart
from Site.app.text.translit.translitPart import translitPart


def replAllType(string=''):
    result = [string]
    inflectResult = [string]
    alterResult = [string]
    decimResult = [string]
    mimicResult = [string]
    translitResult = [string]

    # inflectResult += inflect(string)

    decimResult += decimPart(string)
    # for w in inflectResult:
    #     decimResult += decimPart(w)

    for w in decimResult:
        mimicResult += mimicPart(w)

    for w in mimicResult:
        alterResult += alterPart(w)

    for w in alterResult:
        translitResult += translitPart(w)

    result += inflectResult + decimResult + mimicResult + alterResult + translitResult

    return list(set(result))

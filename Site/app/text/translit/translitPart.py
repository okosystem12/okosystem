from Site.app.text.repl.replPart import replPart
from Site.app.text.translit.translitDict import translitDict


def translitPart(string=''):
    return replPart(string, translitDict())


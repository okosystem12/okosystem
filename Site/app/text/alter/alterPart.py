from Site.app.text.alter.alterDict import alterDict
from Site.app.text.repl.replPart import replPart


def alterPart(string=''):
    return replPart(string, alterDict())

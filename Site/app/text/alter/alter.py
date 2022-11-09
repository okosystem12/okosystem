from Site.app.text.alter.alterDict import alterDict
from Site.app.text.repl.replFull import replFull


def alter(string=''):
    return replFull(string, alterDict())

from Site.app.text.mimic.mimicDict import mimicDict
from Site.app.text.repl.replFull import replFull


def mimic(string=''):
    return replFull(string, mimicDict())

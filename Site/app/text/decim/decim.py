from Site.app.text.decim.decimDict import decimDict
from Site.app.text.repl.replFull import replFull


def decim(string=''):
    return replFull(string, decimDict())

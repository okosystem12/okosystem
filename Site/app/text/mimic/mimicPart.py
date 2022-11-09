from Site.app.text.mimic.mimicDict import mimicDict
from Site.app.text.repl.replPart import replPart


def mimicPart(string=''):
    return replPart(string, mimicDict())

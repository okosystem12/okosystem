from Site.app.control.corruptionList import corruptionList
from Site.app.table.control.value import value


def success(_user):
    return {'controlUser': value(_user), 'corruptList': corruptionList(_user), 'successText': 'Действие выполнено'}

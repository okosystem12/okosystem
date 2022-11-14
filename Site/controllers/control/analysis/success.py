from Site.app.control.corruptionList import corruptionList
from Site.app.status.updateByAnalysis import updateByAnalysis
from Site.app.table.control.value import value


def success(_user):
    updateByAnalysis(_user.first())
    return {
        'controlUser': value(_user),
            'corruptList': corruptionList(_user),
            'successText': 'Действие выполнено',
        'reloadTable': True
    }

from django.db.models import Q

from Site.app.handler.linkList import linklist
from Site.app.handler.valueList import valueList
from Site.models import InfCorrupt


def oneInf(inf):
    return {
        'realId': inf.id,
        'materialsType': 'Личная информация',
        'materials': {
            'type': 'inf',
            'content': [
                {'key': 'О себе', 'value': inf.about},
                {'key': 'Деятельность', 'value': inf.activities},
                {'key': 'Любимые книги', 'value': inf.books},
                {'key': 'Любимые игры', 'value': inf.games},
                {'key': 'Интересы', 'value': inf.interests},
                {'key': 'Любимые фильмы', 'value': inf.movies},
                {'key': 'Любимая музыка', 'value': inf.music},
                {'key': 'Никнейм', 'value': inf.nickname},
                {'key': 'Любимые цитаты', 'value': inf.quotes},
                {'key': 'Статус', 'value': inf.status},
                {'key': 'Любимые телешоу', 'value': inf.tv}
            ]
        }
    }

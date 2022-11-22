def value(oList):
    result = []

    for o in oList:
        result.append({
            'id': o.id,
            'value': o.value,
            'info': o.info,
            'extend_count': o.extend_count,
            'extend_finish': {
                'title': "Подготовка словаря" if o.extend_finish != 100 else "Словарь готов к работе",
                'value': o.extend_finish,
                'color': '#0075ff' if o.extend_finish != 100 else "#5cb85c"
            },
        })

    return result

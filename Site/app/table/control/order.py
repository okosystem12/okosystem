def order(oList, order, order_dir):
    if order == 'fullName':
        return oList.order_by(
            order_dir + 'lastName',
            order_dir + 'firstName',
            order_dir + 'patronymic',
            order_dir + 'pk'
        )
    elif order == 'birthDate':
        return oList.order_by(
            order_dir + 'birthYear',
            order_dir + 'birthMonth',
            order_dir + 'birthDay',
            order_dir + 'pk'
        )
    elif order == 'schools':
        return oList.order_by(
            order_dir + 'schools',
            order_dir + 'pk'
        )
    elif order == 'universities':
        return oList.order_by(
            order_dir + 'universities',
            order_dir + 'pk'
        )
    elif order == 'work':
        return oList.order_by(
            order_dir + 'work',
            order_dir + 'pk'
        )
    elif order == 'vch':
        return oList.order_by(
            order_dir + 'vch__number',
            order_dir + 'pk'
        )
    elif order == 'updatedAt':
        return oList.order_by(
            order_dir + 'updatedAt',
            order_dir + 'pk'
        )
    elif order == 'status':
        return oList.order_by(
            order_dir + 'status__stage__value',
            order_dir + 'status__value',
            order_dir + 'pk'
        )
    return oList

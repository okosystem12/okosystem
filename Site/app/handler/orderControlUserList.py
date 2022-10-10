def orderControlUserList(controlUserList, order, order_dir):
    if order == 'fullName':
        return controlUserList.order_by(
            order_dir + 'lastName',
            order_dir + 'firstName',
            order_dir + 'patronymic',
            order_dir + 'pk'
        )
    elif order == 'birthDate':
        return controlUserList.order_by(
            order_dir + 'birthYear',
            order_dir + 'birthMonth',
            order_dir + 'birthDay',
            order_dir + 'pk'
        )
    elif order == 'schools':
        return controlUserList.order_by(
            order_dir + 'schools',
            order_dir + 'pk'
        )
    elif order == 'universities':
        return controlUserList.order_by(
            order_dir + 'universities',
            order_dir + 'pk'
        )
    elif order == 'work':
        return controlUserList.order_by(
            order_dir + 'work',
            order_dir + 'pk'
        )
    elif order == 'vch':
        return controlUserList.order_by(
            order_dir + 'vch__number',
            order_dir + 'pk'
        )
    return controlUserList

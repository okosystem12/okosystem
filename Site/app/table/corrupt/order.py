def order(oList, order, order_dir):

    if order == 'value':
        oList = oList.order_by(
            order_dir + 'value'
        )
    elif order == 'info':
        oList = oList.order_by(
            order_dir + 'info'
        )

    return oList


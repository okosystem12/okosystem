def order(oList, order, order_dir):
    if order == 'number':
        oList = oList.order_by(
            order_dir + 'number'
        )

    return oList

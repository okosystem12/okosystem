def customList(x, y, key, custom):
    xLen = len(x[key])
    yLen = len(y[key])

    for i in range(xLen if xLen > yLen else yLen):
        if i == xLen:
            return 1
        if i == yLen:
            return -1

        if x[key][i][custom] < y[key][i][custom]:
            return 1
        elif x[key][i][custom] > y[key][i][custom]:
            return -1
    return 0

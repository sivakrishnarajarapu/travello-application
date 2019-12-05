def counts(i, j, m):
    inc = 0
    try:
        if m[i - 1][j - 1] is True:
            inc += 1
    except:
        pass
    try:
        if m[i - 1][j] is True:
            inc += 1
    except:
        pass
    try:
        if m[i - 1][j + 1] is True:
            inc += 1
    except:
        pass
    try:
        if m[i][j + 1] is True:
            inc += 1
    except:
        pass

    try:
        if m[i][j - 1] is True:
            inc += 1
    except:
        pass
    try:
        if m[i + 1][j - 1] is True:
            inc += 1
    except:
        pass
    try:
        if m[i + 1][j + 1] is True:
            inc += 1
    except:
        pass
    try:
        if m[i + 1][j] is True:
            inc += 1
    except:
        pass

    return inc


def minesweeper(m):
    bl = []
    for i in range(0, len(m)):
        sml = []
        for j in range(0, len(m[0])):
            k = counts(i, j, m)
            sml.append(k)
        bl.append(sml)
    return bl
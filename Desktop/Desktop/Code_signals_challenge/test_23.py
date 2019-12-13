def boxBlur(l):
    x=len(l[0])-2
    y=len(l)-2
    b=[[0 for i in range(x)] for j in range(y)]
    for i in range(y):
        for j in range(x):
            b[i][j]=l[i][j]+l[i][j+1]+l[i][j+2]+l[i+1][j]+l[i+1][j+1]+l[i+1][j+2]+l[i+2][j]+l[i+2][j+1]+l[i+2][j+2]
            b[i][j]//=9
    return b
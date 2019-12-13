def fun(n):
    s=0
    t=0
    for i in range(int(len(n)/2)):
        s=s+int(n[i])
    for j in range(int(len(n)/2),len(n)):
        t=t+int(n[j])
    if s==t:
        return True
    else:
        return False
print(fun("1230"))


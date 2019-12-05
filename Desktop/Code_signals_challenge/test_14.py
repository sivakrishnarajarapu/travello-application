def alternatingSums(a):
    s=0
    t=0
    l=[]
    for i in range(0,len(a),2):
        s=s+a[i]
    l.append(s)
    for j in range(1,len(a),2):
        t=t+a[j]
    l.append(t)
    return l


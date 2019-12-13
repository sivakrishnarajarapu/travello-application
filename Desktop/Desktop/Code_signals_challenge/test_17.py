def arrayChange(l):
    c=0
    for i in range(1,len(l)):
        if l[i]<=l[i-1]:
            s=(l[i-1]-l[i])+1
            l[i]=l[i-1]+1
            c+=s
    return c
print(arrayChange([1,7,4]))


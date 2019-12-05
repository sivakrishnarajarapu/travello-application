def fun(s):
    k=[]
    n=3
    for i in range(len(s)):
        if s[i]==1:
            s[i]=n
            k.append(s[i])
        else:
            k.append(s[i])
    print(k)
fun([1,2,1])

# k=[s[i]=3 for i in s if i==1]
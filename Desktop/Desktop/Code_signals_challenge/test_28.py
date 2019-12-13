# m=chr(ord("s")+1)
# print(m)

def fun(s):
    n=''
    for i in s:
        if i=='z':
            n+='a'
        else:
            k=chr(ord(i)+1)
            n+=k
    return n
print(fun("crazy"))


def fun(s):
    st=0
    m=list(s)
    print(m)
    for i in m:
        if m[0].isdigit()!=True and m[0]!=" " and m[0]!="-":
            if i.isalpha() or i.isdigit() or i=="_":
                pass
            else:
                st += 1
        else:
            return False
    if st>0:
        return False
    else:
        return True

print(fun("qq-q"))






def fun(s):
    a = s.split('.')
    print(a)
    if len(a) != 4:
        return False
    for i in a:
        if not i.isdigit():
            return False
        b = int(i)
        if b < 0 or b > 255:
            return False
    return True




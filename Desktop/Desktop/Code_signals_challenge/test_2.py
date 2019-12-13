def centuryFromYear(year):
    x = year / 100
    y = year % 100
    if y == 0:
        return int(x)
    else:
        return int(x) + 1


centuryFromYear(1905)

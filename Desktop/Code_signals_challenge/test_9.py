def allLongestStrings(inputArray):
    l1=[]
    l2=[]
    for i in inputArray:
        l=len(i)
        l1.append(l)
    z=max(l1)
    for i in inputArray:
        if z==len(i):
            l2.append(i)
    return l2
l=["aba", "aa", "ad", "vcd", "aba"]
print(allLongestStrings(l))
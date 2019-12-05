# Given a sorted array of integers a, your task is to determine which element of a is closest to all other values of a.
# In other words, find the element x in a, which minimizes the following sum:
# abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
# (where abs denotes the absolute value)
# If there are several possible answers, output the smallest one.
# For a = [2, 4, 7], the output should be absoluteValuesSumMinimization(a) = 4.
#
# for x = 2, the value will be abs(2 - 2) + abs(4 - 2) + abs(7 - 2) = 7.
# for x = 4, the value will be abs(2 - 4) + abs(4 - 4) + abs(7 - 4) = 5.
# for x = 7, the value will be abs(2 - 7) + abs(4 - 7) + abs(7 - 7) = 8.
# The lowest possible value is when x = 4, so the answer is 4.
#
# For a = [2, 3], the output should be absoluteValuesSumMinimization(a) = 2.
#
# for x = 2, the value will be abs(2 - 2) + abs(3 - 2) = 1.
# for x = 3, the value will be abs(2 - 3) + abs(3 - 3) = 1.
# Because there is a tie, the smallest x between x = 2 and x = 3 is the answer.

# 32

def absoluteValuesSumMinimization(a):
    c=0
    k={}
    for i in a:
        for j in range(len(a)):
            s=abs(i-a[j])
            c+=s
        k[i]=c
        c=0
    # m=min(k)
    # return m
    return min(k, key=lambda x:k[x])
print(absoluteValuesSumMinimization([2,4,7]))





# 33

from itertools import permutations

def stringchk(x, y):
    c = 0
    d = 0
    e = -1
    for i in x:
        e += 1
        if i in y[e]:
            c += 1
    return c

def stringsRearrangement(i):
    h = 0
    l = list(permutations(i))
    for i in range(len(l)):
        f = 0
        for j in range(len(l[i]) - 1):
            z = stringchk(l[i][j], l[i][j + 1])
            if z == len(l[i][j]) - 1:
                f += 1
        if f == len(l[0]) - 1:
            return True
        else:
            h += 1
            if h == len(l):
                return False
print(stringsRearrangement(["aba", "bbb", "bab"]))
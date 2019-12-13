# def digSum(n):
#     sum = 0
#     while (n > 0 or sum > 9):
#         if (n == 0):
#             n = sum
#             sum = 0
#         sum += n % 10
#         n /= 10
#     return int(sum)
# print(digSum(99))


def digisum(n):
    if n==0:
        return 0
    if n%9==0:
        return 9
    else:
        return int(n%9)
print(digisum(73))

def digitDegree(n):
    t=0
    # n=0
    while len(str(n))>1:
        t+=1
        s=0
        for i in str(n):
            s+=int(i)
        n=s
    return t

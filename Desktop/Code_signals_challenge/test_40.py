# def longestDigitsPrefix(s):
#     digit = ''
#     for x in s:
#         if x.isdigit():
#             digit+=x
#         else:
#             break
#     return digit
# print(longestDigitsPrefix("122323aa1"))


def digitDegree(n):
    t = 0
    # n=0
    while len(str(n)) > 1:
        t += 1
        s = 0
        for i in str(n):
            s += int(i)
        n = s
    return t
print(digitDegree(91))


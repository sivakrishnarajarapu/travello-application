# def fun(s):
#     b=max(s)
#     n=1
#     print(b)
#     for i in range(0,b+1):
#         if i not in s:
#             return n
#         else:
#             n+=1
#
#     print(n)
# fun([5,8,9,13,14])

# def fun(s):
#     n=1
#     while True:
#         n += 1
#         for i in s:
#             if i%n==0:
#                 break
#         else:
#             return n
# print(fun([5,3,6,7,9]))


# ls=[1,5,8,5,6,5,6]
# ls.sort()
# print(ls)
# l=set(ls)
# print(l)
# k=list(l)
# print(k)
# m=sort()
# k=set(l)
# print(l)
# n=int(input())
# s=map(int,(input().split()))
# print(sorted(list(set(s)))[-2])

# s="Hello world"
s="123"
count=0
alpha=0
for i in s:
    if i==' ':
        continue
    elif i.isdigit():
        count+=1
    else:
        alpha+=1
print(count)
print(alpha)

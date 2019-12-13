# def fun(st1):
#     st1.sort()
#     a=min(st1)
#     b=max(st1)
#     result=0
#     x=list(range(a,b+1))
#     for i in x:
#         if i in st1:
#             pass
#         else:
#             result += 1
#     return result
# z=fun([6,3,2,8])
# print(z)





#def fun(st1):

def fun(n):
    a=max(n)
    b=min(n)

    return a-b+1-len(n)
print(fun([1,5,2,7]))






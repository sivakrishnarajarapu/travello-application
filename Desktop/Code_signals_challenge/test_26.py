# def fun(s):
#     m=list(s)
#     n=[int(i) for i in m]
#     # print(n)
#     for i in n:
#         if i%2!=0:
#             return False
#         else:
#             return True
#
#
#
#     # k=[True for i in n if i%2==0]
#     # print(k)
#     # # for i in n:
#
# print(fun("248622"))

def fun(s):
    for i in str(s):
        if int(i)%2!=0:
            return False
    else:
        return True

print(fun("2487622"))





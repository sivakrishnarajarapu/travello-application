# def reverseInParentheses(a):
#     l=list(a)
#     l1=[]
#     l2=[]
#     l5=[]
#     c=-1
#     w=''
#     for i in range(len(l)):
#         if l[i]=='(' or l[i]==')':
#             l1.append(i)
#     p=l1[0]
#     q=l1[1]
#     l3=list(l[p+1:q])
#     l4=(list(reversed(l3)))
#     for i in range(len(l)):
#         if i not in range(p,q+1):
#             l5.append(l[i])
#         elif i in range(p+1,q):
#             c+=1
#             l5.append(l4[c])
#     for x in l5:
#         w+=x
#     return w
# print(reverseInParentheses("(Hello)"))

# def reverseInParentheses(s):
#     for i in range(len(s)):
#         if s[i] == "(":
#             start = i
#         if s[i] == ")":
#             end = i
#             return reverseInParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
#     return s
# print(reverseInParentheses("()"))



def fun(s):
    while ')' in s:
        a=s.find(')')
        b=s[:a].rfind('(')
        c=s[b+1:a][::-1]
        s=s[:b]+c+s[a+1:]
    return s
print(fun("foo(bar(baz))blim"))







# def fun(s):
#     while ')' in s:
#         l=s.index(')')
#         k=s.rfind('(')
#
#         d=s[l+1:k][::-1]
#         print(d)
#         k=s[:l]+d+s[k+1:]
#         print(k)
#         break
#
#     return k


        # for i in s:
        #     print(i)






        # return print(s.rfind('('))






# print(fun("foo(bar(baz))blim"))
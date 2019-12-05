# def reverseParentheses(s):
#     if '(' in s:
#         posopen=s.find('(')
#         s=s[:posopen]+reverseParentheses(s[posopen+1:])
#         posclose=s.find(')',posopen+1)
#         s=s[:posopen]+s[posopen:posclose][::-1]+s[posclose+1:]
#     return s
#
# string='a(bcdefghijkl(mno)p)q'
# print(string)
# print(reverseParentheses(string))
# print('apmnolkjihgfedcbq') # your test
#
# string='a(bc)(ef)g'
# print(string)
# print(reverseParentheses(string))


def variableName(var):
    c=0
    l=list(str(var))
    for i in l:
        if l[0].isdigit()!=True and l[0]!=' ':
            if i.isalpha() or i.isdigit() or i == "_":
                pass
            else:
                c+=1
        else:
            return False
    # if c>0:
    #     return False
    # else:
    #     return True
print(variableName(("var_1__Int")))
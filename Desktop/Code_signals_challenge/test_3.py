def checkPalindrome(inputString):
 l = len(inputString)
 p = l - 1
 index = 0
 while index < p:
    if inputString[index] == inputString[p]:
        index = index + 1
        p = p - 1
        print("String is a palindrome")
        break
    else:
        print("string is not a palindrome")
        break

checkPalindrome("mam")


# def checkPalindrome(inputString):
#     if inputString == inputString[::-1]:
#         return True
#     else:
#         return False
# checkPalindrome("malayalam")
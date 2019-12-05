#1.Write a function that returns the sum of two numbers.
# For param1 = 1 and param2 = 2, the output should be
# add(param1, param2) = 3

# def add(param1, param2):
#     return param1+param2
# add(1,4)

# 2.Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100,
# the second - from the year 101 up to and including the year 200, etc.
# For year = 1905, the output should be
# centuryFromYear(year) = 20;
# For year = 1700, the output should be
# centuryFromYear(year) = 17

# def centuryFromYear(year):
#     return (year - 1) // 100 + 1
# print(centuryFromYear(2017))


#3.Given the string, check if it is a palindrome.
# For inputString = "aabaa", the output should be
# checkPalindrome(inputString) = true;
# For inputString = "abac", the output should be
# checkPalindrome(inputString) = false;
# For inputString = "a", the output should be
# checkPalindrome(inputString) = true.

# def checkPalindrome(inputstring):
#     if inputstring == inputstring[::-1] :
#         return True
#     else :
#         return False

#4.Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
# For inputArray = [3, 6, -2, -5, 7, 3], the output should be
# adjacentElementsProduct(inputArray) = 21.
# 7 and 3 produce the largest product.

# def adjacentElementsProduct(inputArray):
#     l1 = []
#     for i in range(len(inputArray) - 1):
#         x = inputArray[i] * inputArray[i + 1]
#         l1.append(x)
#     y = max(l1)
#     return y
# adjacentElementsProduct([3, 6, -2, -5, 7, 3])


#5.Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.
# A 1-interesting polygon is just a square with a side of length 1.
# An n-interesting polygon is obtained by taking the n - 1-interesting polygon and
# appending 1-interesting polygons to its rim, side by side.
# You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

# def shapeArea(n):
#     area = (n**2)+((n-1)**2)
#     return area
# shapeArea(2)

#6.Ratiorg got statues of different sizes as a present from CodeMaster for his birthday,
# each statue having an non-negative integer size. Since he likes to make things perfect,
# he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1.
# He may need some additional statues to be able to accomplish that.
# Help him figure out the minimum number of additional statues needed.
# For statues = [6, 2, 3, 8], the output should be
# makeArrayConsecutive2(statues) = 3.
# Ratiorg needs statues of sizes 4, 5 and 7.

# def makeArrayConsecutive2(statues):
#     count=0
#     for i in range(min(statues),max(statues)+1):
#         if i not in statues:
#             count+=1
#     return count

#7.Given a sequence of integers as an array,
# determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

# Note: sequence a0, a1, ..., an is considered to be a strictly increasing
# if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

# For sequence = [1, 3, 2, 1], the output should be
# almostIncreasingSequence(sequence) = false.

# There is no one element in this array that can be removed in order to get a strictly increasing sequence.

# For sequence = [1, 3, 2], the output should be
# almostIncreasingSequence(sequence) = true.

# You can remove 3 from the array to get the strictly increasing sequence [1, 2].
# Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

# def almostIncreasingSequence(sequence):
#     droppped = False
#     last = prev = min(sequence) - 1
#     for elm in sequence:
#         if elm <= last:
#             if droppped:
#                 return False
#             else:
#                 droppped = True
#             if elm <= prev:
#                 prev = last
#             elif elm >= prev:
#                 prev = last = elm
#         else:
#             prev, last = last, elm
#     return True


#8.After becoming famous, the CodeBots decided to move into a new building together.
# Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted!
# Since the CodeBots are quite superstitious,
# they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

# Given matrix, a rectangular matrix of integers, where each value represents the cost of the room,
# your task is to return the total sum of all rooms that are suitable for the CodeBots
# (ie: add up all the values that don't appear below a 0).

# matrix = [[0, 1, 1, 2],
#           [0, 5, 0, 0],
#           [2, 0, 3, 3]]
# the output should be
# matrixElementsSum(matrix) =
# There are several haunted rooms,
# so we'll disregard them as well as any rooms beneath them.
# Thus, the answer is 1 + 5 + 1 + 2 = 9.

# def matrixElementsSum(matrix):
#     t=0
#     for j in range(0,len(matrix[0])):
#         for i in range(0,len(matrix)):
#             if matrix[i][j]==0:
#                 break
#             else:
#                 t+=matrix[i][j]
#     return t


#9.Given an array of strings, return another array containing all of its longest strings.
# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

#  def allLongestStrings(inputArray):
#     l1=[]
#     l2=[]
#     for i in inputArray:
#         l=len(i)
#         l1.append(l)
#     z=max(l1)
#     for i in inputArray:
#         if z==len(i):
#             l2.append(i)
#     return l2


#10.Given two strings, find the number of common characters between them.
# For s1 = "aabcc" and s2 = "adcaa", the output should be
# commonCharacterCount(s1, s2) = 3.
# Strings have 3 common characters - 2 "a"s and 1 "c".

# def commonCharacterCount(s1, s2):
#     a=[min(s1.count(i),s2.count(i))for i in set(s1)]
#     return sum(a)

#11.Ticket numbers usually consist of an even number of digits.
# A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
# Given a ticket number n, determine if it's lucky or not.
#For n = 1230, the output should be
# isLucky(n) = true;
# For n = 239017, the output should be
# isLucky(n) = false.

# def isLucky(m):
#     n=str(m)
#     s=0
#     t=0
#     for i in range(int(len(n)/2)):
#         s=s+int(n[i])
#     for j in range(int(len(n)/2),len(n)):
#         t=t+int(n[j])
#     if s==t:
#         return True
#     else:
#         return False

#12.Some people are standing in a row in a park. There are trees between them which cannot be moved.
# Your task is to rearrange the people by their heights in a non-descending order without moving the trees.
# People can be very tall!
# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

# def sortByHeight(a):
#     l1=[]
#     l2=[]
#     l4=[]
#     c=-1
#     for i in range(len(a)):
#         if a[i]==-1:
#             l1.append(i)
#         else:
#             l2.append(a[i])
#     l3=sorted(l2)
#     for j in range(len(a)):
#         k=j
#         if j in l1:
#             l4.append(-1)
#         else:
#             c+=1
#             l4.append(l3[c])
#     return l4


# 13.Write a function that reverses characters in (possibly nested) parentheses in the input string.
# Input strings will always be well-formed with matching ()s.

# For inputString = "(bar)", the output should be
# reverseInParentheses(inputString) = "rab";
# For inputString = "foo(bar)baz", the output should be
# reverseInParentheses(inputString) = "foorabbaz";
# For inputString = "foo(bar)baz(blim)", the output should be
# reverseInParentheses(inputString) = "foorabbazmilb";
# For inputString = "foo(bar(baz))blim", the output should be
# reverseInParentheses(inputString) = "foobazrabblim".
# Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim"

# def reverseInParentheses(inputString):
#     for i in range(len(inputString)):
#         if inputString[i] == "(":
#             start = i
#         if inputString[i] == ")":
#             end = i
#             return reverseInParentheses(inputString[:start] + inputString[start+1:end][::-1] + inputString[end+1:])
#     return inputString
# print(reverseInParentheses("()"))


# 14.Several people are standing in a row and need to be divided into two teams.
# The first person goes into team 1, the second goes into team 2,
# the third goes into team 1 again, the fourth into team 2, and so on.
# You are given an array of positive integers - the weights of the people.
# Return an array of two integers, where the first element is the total weight of team 1,
# and the second element is the total weight of team 2 after the division is complete.

# For a = [50, 60, 60, 45, 70], the output should be
# alternatingSums(a) = [180, 105].

# def alternatingSums(a):
#     s1=0
#     s2=0
#     l=[]
#     for i in range(0,len(a),2):
#         s1+=a[i]
#     l.append(s1)
#     for j in range(1,len(a),2):
#         s2+=a[j]
#     l.append(s2)
#     return l


# 15.Given a rectangular matrix of characters, add a border of asterisks(*) to it.
# picture = ["abc",
#            "ded"]
# the output should be
#
# addBorder(picture) = ["*****",
#                       "*abc*",
#                       "*ded*",
#                       "*****"]


#  def addBorder(p):
#     l=-1
#     l2=[]
#     l3=''
#     l4=[]
#     for i in range(len(p)+2):
#         if i in range(1,len(p)+1):
#             for j in range(len(p[0])+2):
#                 if j in range(1,len(p[0])+1):
#                     l+=1
#                     l3+=str(p[i-1][l])
#                 else:
#                     l3+='*'
#             l2.append(l3)
#             l3=''
#             l=-1
#         else:
#             for j in range(len(p[0])+2):
#                 l3+='*'
#             l2.append(l3)
#             l3 = ''
#     l4.extend(l2)
#     l2=[]
#     return l4
# print(addBorder(["abc","def"]))
#


# 16.Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.
# Given two arrays a and b, check whether they are similar.
#For a = [1, 2, 3] and b = [1, 2, 3], the output should be
# areSimilar(a, b) = true.
# The arrays are equal, no need to swap any elements.
# For a = [1, 2, 3] and b = [2, 1, 3], the output should be
# areSimilar(a, b) = true.
# We can obtain b from a by swapping 2 and 1 in b.
# For a = [1, 2, 2] and b = [2, 1, 1], the output should be
# areSimilar(a, b) = false.
# Any swap of any two elements either in a or in b won't make a and b equal.

#def areSimilar(a, b):
    # d=[]
    # if a!=b:
    #     if len(a)==len(b):
    #         for i in range(len(a)):
    #             if a[i]!=b[i]:
    #                 d.append(i)
    #                 print(d)
    #     else:
    #         return False
    #     if len(d)==2 and a[d[0]]==b[d[1]] and a[d[1]]==b[d[0]]:
    #         return True
    #     else:
    #         return False
    # else:
    #     return True

# 17.You are given an array of integers. On each move you are allowed to increase exactly one of its element by one.
# Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
# For inputArray = [1, 1, 1], the output should be
# arrayChange(inputArray) = 3.

# def arrayChange(l):
#     c=0
#     for i in range(1,len(l)):
#         if l[i]<=l[i-1]:
#             s=(l[i-1]-l[i])+1
#             l[i]=l[i-1]+1
#             c+=s
#     return c


# 18.Given a string, find out if its characters can be rearranged to form a palindrome.
# For inputString = "aabb", the output should be
# palindromeRearranging(inputString) = true.
# We can rearrange "aabb" to make "abba", which is a palindrome.

# from collections import Counter
# def palindromeRearranging(s):
#     k=0
#     c=Counter(s)
#     for i in c.values():
#         if i%2!=0:
#             k+=1
#         else:
#             pass
#     if k<=1:
#         return True
#     else:
#         return False
# print(palindromeRearranging("aabb"))


# 19.Call two arms equally strong if the heaviest weights they each are able to lift are equal.

# Call two people equally strong if their strongest arms are equally strong
# (the strongest arm can be both the right and the left),
# and so are their weakest arms.
# Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

# For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10, the output should be
# areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
# For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 10, the output should be
# areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
# For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 9, the output should be
# areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = false.

# def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
#     if yourLeft==friendsLeft and yourRight==friendsRight:
#         return True
#     elif yourLeft==friendsRight and yourRight==friendsLeft:
#         return True
#     else:
#         return False

# 20.Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
# For inputArray = [2, 4, 1, 0], the output should be
# arrayMaximalAdjacentDifference(inputArray) = 3.

# def arrayMaximalAdjacentDifference(inputArray):
#     max=0
#     for i in range(1,len(inputArray)):
#         if abs(inputArray[i]-inputArray[i-1])>max:
#               max=abs(inputArray[i]-inputArray[i-1])
#     return max

#         For inputString = "172.16.254.1", the output should be



#21.An IP address is a numerical label assigned to each device (e.g., computer, printer)
# participating in a computer network that uses the Internet Protocol for communication.
# There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.
# Given a string, find out if it satisfies the IPv4 address naming rules.

# For inputString = "172.316.254.1", the output should be
# isIPv4Address(inputString) = false.
# 316 is not in range [0, 255].
# For inputString = ".254.255.0", the output should be
# isIPv4Address(inputString) = false.
# There is no first number.


# def isIPv4Address(inputString):
#     max=255
#     a=inputString.split('.')
#     if len(a)!=4:
#         return False
#     for i in a:
#         if not i.isdigit():
#             return False
#         i=int(i)
#         if i<0 or i>255:
#             return False
#     return True

# 22.You are given an array of integers representing coordinates of obstacles situated on a straight line.
# Assume that you are jumping from the point with coordinate 0 to the right.
# You are allowed only to make jumps of the same length represented by some integer.
# Find the minimal length of the jump enough to avoid all the obstacles.

# For inputArray = [5, 3, 6, 7, 9], the output should be
# avoidObstacles(inputArray) = 4.
# Check out the image below for better understanding:

# def avoidObstacles(inputArray):
#     n=1
#     while True:
#         n += 1
#         for i in inputArray:
#             if i%n==0:
#                 break
#         else:
#             return n


#23.Last night you partied a little too hard.
# Now there's a black and white photo of you that's about to go viral! You can't let this ruin your reputation,
# so you want to apply the box blur algorithm to the photo to hide its content.

# The pixels in the input image are represented as integers.
# The algorithm distorts the input image in the following way:
# Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3
# square that has its center at x, including x itself. All the pixels on the border of x are then removed.

# Return the blurred image as an integer, with the fractions rounded down.
# For
# image = [[1, 1, 1],
#          [1, 7, 1],
#          [1, 1, 1]]
# the output should be boxBlur(image) = [[1]].
# To get the value of the middle pixel in the input 3 × 3 square: (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1.
# The border pixels are cropped from the final result.
# For
# image = [[7, 4, 0, 1],
#          [5, 6, 2, 2],
#          [6, 10, 7, 8],
#          [1, 4, 2, 0]]
# the output should be
#
# boxBlur(image) = [[5, 4],
#                   [4, 4]]
# There are four 3 × 3 squares in the input image, so there should be four integers in the blurred output.
# To get the first value: (7 + 4 + 0 + 5 + 6 + 2 + 6 + 10 + 7) = 47 / 9 = 5.2222 = 5.
# The other three integers are obtained the same way, then the surrounding integers are cropped from the final result.

# def boxBlur(l):
#     x=len(l[0])-2
#     y=len(l)-2
#     b=[[0 for i in range(x)] for j in range(y)]
#     for i in range(y):
#         for j in range(x):
#             b[i][j]=l[i][j]+l[i][j+1]+l[i][j+2]+l[i+1][j]+l[i+1][j+1]+l[i+1][j+2]+l[i+2][j]+l[i+2][j+1]+l[i+2][j+2]
#             b[i][j]//=9
#     return b


# 24.In the popular Minesweeper game you have a board with s
# ome mines and those cells that don't contain a mine have a number in it that indicates
# the total number of mines in the neighboring cells.
# Starting off with some arrangement of mines we want to create a Minesweeper game setup.

# For
# matrix = [[true, fadef counts(i,j,m):
#     inc = 0
#     try:
#         if i-1>=0 and j-1>=0 and  m[i - 1][j - 1] == True:
#             inc += 1
#     except:
#         pass
#     try:
#         if i-1>=0 and j>=0 and m[i - 1][j] == True:
#             inc += 1
#     except:
#         pass
#     try:
#         if i-1>=0 and j+1>=0 and m[i - 1][j + 1] == True:
#             inc += 1
#     except:
#         pass
#     try:
#         if i>=0 and j+1>=0 and m[i][j + 1] == True:
#             inc += 1
#     except:
#         pass
#
#     try:
#         if i>=0 and j-1>=0 and m[i][j - 1] == True:
#             inc += 1
#     except:
#         pass
#     try:
#         if i+1>=0 and j-1>=0 and m[i + 1][j - 1] == True:
#             inc += 1
#     except:
#         pass
#     try:
#         if i+1>=0 and j+1>=0 and m[i + 1][j + 1] == True:
#             inc += 1
#     except:
#         pass
#     try:
#         if i+1>=0 and j>=0 and m[i + 1][j] == True:
#             inc += 1
#     except:
#         pass
#
#     return inc

# def minesweeper(m):
#     bl = []
#     for i in range(0, len(m)):
#         sml = []
#         for j in range(0, len(m[0])):
#             sml.append(counts(i,j,m))
#         bl.append(sml)
#     return bllse, false],
#           [false, true, false],
#           [false, false, false]]
# the output should be
# minesweeper(matrix) = [[1, 2, 1],
#                        [2, 1, 1],
#                        [1, 1, 1]]

# 25.Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.
# For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be
# arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].

# def arrayReplace(inputArray, elemToReplace, substitutionElem):
#     k=[]
#     for i in range(len(inputArray)):
#         if inputArray[i]==elemToReplace:
#             inputArray[i]=substitutionElem
#             k.append(inputArray[i])
#         else:
#             k.append(inputArray[i])
#     return k

# 26.Check if all digits of the given integer are even.

# For n = 248622, the output should be
# evenDigitsOnly(n) = true;
# For n = 642386, the output should be
# evenDigitsOnly(n) = false.

# def evenDigitsOnly(n):
#     for i in str(n):
#         if int(i)%2!=0:
#             return False
#     else:
#         return True

# 27.Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.
# Check if the given string is a correct variable name.

# For name = "var_1__Int", the output should be
# variableName(name) = true;
# For name = "qq-q", the output should be
# variableName(name) = false;
# For name = "2w2", the output should be
# variableName(name) = false.

# def variableName(name):
#     st=0
#     m=list(str(name))
#     print(m)
#     for i in m:
#         if m[0].isdigit()!=True and m[0]!=" ":
#             if i.isalpha() or i.isdigit() or i=="_":
#                 pass
#             else:
#                 st+=1
#         else:
#             return False
#     if st>0:
#         return False
#     else:
#         return True

# 28.Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e.
# replace a with b, replace b with c, etc (z would be replaced by a).
# For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".

# def alphabeticShift(inputString):
#     n=''
#     for i in inputString:
#         if i=='z':
#             n+='a'
#         else:
#             k=chr(ord(i)+1)
#             n+=k
#     return n

# 30.Consider integer numbers from 0 to n - 1 written down along the circle in such a way that
# the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

# Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

# For n = 10 and firstNumber = 2, the output should be
# circleOfNumbers(n, firstNumber) = 7.

# def circleOfNumbers(n, firstNumber):
#     s=int(n/2)
#     l=[]
#     for i in range(0,n):
#         l.append(i)
#     l1=l[0:s]
#     l2=l[s:]
#     for i in range(len(l1)):
#         if l1[i]==firstNumber:
#             return l2[i]
#         else:
#             for j in range(len(l2)):
#                 if l2[j]==firstNumber:
#                     return l1[j]


# 31.You have deposited a specific amount of money into your bank account.
# Each year your balance increases at the same growth rate. With the assumption that you don't make any additional deposits,
# find out how long it would take for your balance to pass a specific threshold.

# For deposit = 100, rate = 20, and threshold = 170, the output should be
# depositProfit(deposit, rate, threshold) = 3.
# Each year the amount of money in your account increases by 20%. So throughout the years, your balance would be:
# year 0: 100;
# year 1: 120;
# year 2: 144;
# year 3: 172.8.
# Thus, it will take 3 years for your balance to pass the threshold, so the answer is 3.

# def depositProfit(deposite, rate, threshold):
#     year=0
#     while deposite<threshold:
#         deposite=deposite+(deposite*(rate/100))
#         year+=1
#     return year


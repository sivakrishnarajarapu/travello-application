# def centuryFromYear(year):
#     return (year - 1) // 100 + 1
#
# print(centuryFromYear(2017))
#

# 29

def chessBoardCellColor(c1, c2):
    l1=['A','B','C','D','E','F','G','H']
    c=l1.index(c1[0])+1
    d=l1.index(c2[0])+1
    if c%2==0 and int(c1[1])%2==0 and d%2==0 and int(c2[1])%2==0:
        return  True
    elif c%2!=0 and int(c1[1])%2!=0 and d%2!=0 and int(c2[1])%2!=0:
        return True
    elif c%2!=0 and int(c1[1])%2!=0 and d%2==0 and int(c2[1])%2==0 or c%2==0 and int(c1[1])%2==0 and d%2!=0 and int(c2[1])%2!=0:
        return True
    else:
        return False



# 30

def circleOfNumbers(n, firstNumber):
    n = int(n)
    l = list(range(n))
    l1 = l[0:int(n / 2)]
    l2 = l[int(n / 2):n]
    for i in range(len(l1)):
        if l1[i] == firstNumber:
            return l2[i]
        else:
            for j in range(len(l2)):
                if l2[j] == firstNumber:
                    return l1[j]


# 31

def depositProfit(deposit, rate, threshold):
    years=0
    while deposit<threshold:
        deposit=deposit+(deposit*(rate/100))
        years+=1
    return years



# 32

def absoluteValuesSumMinimization(a):
    d={}
    c=0
    for i in a:
        for j in a:
            b=abs(j-i)
            c+=b
        d[i]=c
        c=0
    return min(d, key=lambda x: d[x])


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


# 34

def extractEachKth(inputArray, k):
    l=[]
    f=0
    for i in range(len(inputArray)):
        f+=1
        if f==k:
            f = 0
            continue
        else:
            l.append(inputArray[i])
    return l

# 35

def firstDigit(inputString):
    for i in inputString:
        if i.isdigit():
            return i


# 36

def differentSymbolsNaive(s):
    return len(set(s))
print(differentSymbolsNaive("acabddb"))


# 37

def arrayMaxConsecutiveSum(l, k):
    t=0
    for i in range(0,len(l)-k):
        e=sum(l[i:i+k])
        if t<e:
            t=e
    return t



# 38







# 39








# 40

def longestDigitsPrefix(s):
    digit = ''
    for x in inputString:
        if x.isdigit():
            digit+=x
        else:
            break
    return digit


# 41

def digitDegree(n):
    t=0
    while len(str(n))>1:
        t+=1
        s=0
        for i in str(n):
            s+=int(i)
        n=s
    return t


# 42



# 43

from collections import Counter
def isBeautifulString(inputString):
    c=dict(Counter(inputString))
    print(c)
    l=[]
    s=0
    m=0
    for i in c.values():
        print(i)
        l.append(i)
    for i in c.keys():
        s+=1
        if s<=len(c)-1 and c[i]>=l[s]:
            pass
        else:
            m+=1
    if m>1:
        return False
    else:
        return True


# 44

def findEmailDomain(address):
    for i in range(len(address)):
        if address[i]=='@':
            if address[i+1].isalpha():
                return address[i+1:]

# 45



# 46

from collections import Counter
def electionsWinners(votes, k):
    winners=0
    maxvotes=max(votes)
    rep=dict(Counter(votes))
    if rep[maxvotes]==1 and k==0:
        winners+=1
        return winners
    else:
        for i in votes:
            if k+i>maxvotes:
                winners+=1
        return winners


# 47

def isMAC48Address(inputString):
    c=0
    d=0
    e=0
    for i in range(1,len(inputString)):
        if inputString[i]=='-':
            e+=1
            continue
        elif inputString[i-1] in '0123456789' or inputString[i] in 'ABCDEF':
            c+=1
            d+=1
        if c>2:
            return False
        else:
            return True
        c=0
    if d==12 and e==5:
        return True
    else:
        return False

# 48


def isDigit(symbol):
    if symbol in ('1','2','3','4','5','6','7','8','9','0'):
        return True
    else:
        return False

# 49

def lineEncoding(s):
    finalstring=''
    elementcount=-1
    numberco=0
    for i in s[numberco:]:
        numbercount=0
        elementcount+=1
        for j in s[numberco:]:
            if i==j:
                numbercount+=1
            else:
                break
        if numbercount==0:
            continue
        elif numbercount==1:
            numberco+=numbercount
            finalstring+=str(i)
        else:
            numberco+=numbercount
            finalstring+=str(numbercount)+str(i)
    return finalstring



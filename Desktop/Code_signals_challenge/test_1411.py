# def fun(n):
#     ls1=0
#     ls2=0
#     l=[]
#     for i in range(0,len(n),2):
#         # if i%2!=0:
#         ls1=ls1+n[i]
#     l.append(ls1)
#     for j in range(1,len(n),2):
#         # if i%2==0:
#         ls2=ls2+n[j]
#     l.append(ls2)
#     return l
#
# print(fun([50, 60, 60, 45, 70]))

# print(type(3/4))


# def findArea(a, b, c):
#     # must be smaller than third side.
#     if (a < 0 or b < 0 or (a + b <= c) or (a + c <= b) or (b + c <= a)):
#         print('Not a valid trianglen')
#         return
#
#     # calculate the semi-perimeter
#     s = (a + b + c) / 2
#
#     # calculate the area
#     area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#     print('Area of a traingle is %f' % area)
# print(findArea([0,0],[3,3],[6,0]))

# import math
# a=int(input("Enter first side: "))
# b=int(input("Enter second side: "))
# c=int(input("Enter third side: "))
# s=(a+b+c)/2
# area=math.sqrt(s*(s-a)*(s-b)*(s-c))
# print("Area of the triangle is: ",round(area,2))

# import math
#
# def distance(x1,y1,x2,y2):
#     length=math.sqrt((x1-x2)**2+(y1-y2)**2)
#     return length
#
# x=[0,3,6]
# y=[0,3,0]
# l=[]
# for i,j in zip(x,y):
#     l.append([i,j])
# print(l)
# a=l[0]
# b=l[1]
# c=l[2]
# s1=distance(a[0],a[1],b[0],b[1])
# s2=distance(a[0],a[1],c[0],c[1])
# s3=distance(b[0],b[1],c[0],c[1])
# sp=(s1+s2+s3)/2
# area=math.sqrt(sp*(sp-s1)+(sp-s2)+(sp-s3))
# print(area)

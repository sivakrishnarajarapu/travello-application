# def shapeArea(n):
#     n=int(n)
#     return ((n**2)+((n-1)**2))
# shapeArea(3)


def shapearea(n):
    area=1
    while n>1:
        area += (n-1)*4
        n-=1
    return area
print(shapearea(2))



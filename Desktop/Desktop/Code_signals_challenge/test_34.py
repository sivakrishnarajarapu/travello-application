# def extractEachKth(inputArray, k):
#     # print(type(inputArray))
#     d=[]
#     for i in range(len(inputArray)):
#         if i%k==0:
#             d.append(inputArray[i])
#         else:
#             continue
#     print(d)
# extractEachKth([2, 4, 6, 8, 10],2)


def extractEachKth(inputArray, k):
    d=[]
    for i in range(0,len(inputArray)):
        if (i+1)%k==0:
            continue
        else:
            d.append(inputArray[i])
    return d
print(extractEachKth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))
# def arrayMaxConsecutiveSum(inputArray, k):
#     s=[]
#     for i in range(len(inputArray)):
#
#         b=inputArray[i]+k
#         s.append(b)
#     print(s)
# arrayMaxConsecutiveSum([2, 3, 5, 1, 6],2)



def arrayMaxConsecutiveSum(ls,k):
    first = sum(ls[0:k])
    maximo = first
    for i in range(k, len(ls)):
        # Just add the last item and erase the first one
        breakpoint()
        first = first - ls[i - k] + ls[i]
        if first > maximo:
            maximo = first
    return maximo
arrayMaxConsecutiveSum([2, 3, 5, 1, 6],2)

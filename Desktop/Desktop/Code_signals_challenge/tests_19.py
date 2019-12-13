def arrayMaximalAdjacentDifference(inputArray):
    max=0
    for i in range(1,len(inputArray)):
        if abs(inputArray[i]-inputArray[i-1])>max:
            max=abs(inputArray[i]-inputArray[i-1])
    return max
print(arrayMaximalAdjacentDifference([10,11,16,13]))

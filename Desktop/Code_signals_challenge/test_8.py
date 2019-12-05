def matrixElementsSum(matrix):
    count=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                for k in range(1,len(matrix)):
                    matrix[k][j]=0
            else:
                count+=matrix[i][j]
    return count
l=[[0,1,1,2],[0,5,0,0],[2,0,3,3]]
print(matrixElementsSum(l))


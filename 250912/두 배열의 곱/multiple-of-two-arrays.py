matrix1 = []
matrix2 = []

for _ in range(3) :
    row_data = list(map(int, input().split()))
    matrix1.append(row_data)

dummy = input()

for _ in range(3) :
    row_data = list(map(int, input().split()))
    matrix2.append(row_data)

endMatrix = []
for i in range(3) :
    tmpList = []
    for j in range(3) : 
        tmpList.append(matrix1[i][j] * matrix2[i][j])
    endMatrix.append(tmpList)

for i in range(3) :
    for j in range(3) : 
        print(endMatrix[i][j], end=' ')
    print()
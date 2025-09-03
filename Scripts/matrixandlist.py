matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
for i in range (len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])

#another method        

for i in matrix:
    for j in i:
        print(j)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end='')
    print()
    
# Transpose a Matrix
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transpose = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transpose[j][i] = matrix[i][j]

print("Transpose of Matrix:")
for row in transpose:
    print(row)

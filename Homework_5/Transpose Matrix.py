def transpose(matrix):
    row = len(matrix)
    col = len(matrix[0])

    transpose_matrix = []

    for i in range(col):
        new_row = []
        for j in range(row):
            new_row.append(matrix[j][i])
        transpose_matrix.append(new_row)


    return transpose_matrix



matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(transpose(matrix))




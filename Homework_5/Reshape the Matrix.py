def reshape(matrix, r, c):

    # return matrix if len(matrix) * len(matrix[0]) != r * c else [
    #     [matrix[(i * c + j) // len(matrix[0])][(i * c + j) % len(matrix[0])] for j in range(c)] for i in range(r)]

    row = len(matrix)
    col = len(matrix[0])

    if row * col != r * c:
        return matrix

    new_matrix = []
    for i in range(row):
        for j in range(col):
            new_matrix.append(matrix[i][j])

    reshaped_matrix = []

    k = 0
    for i in range(r):
        new_row = []
        for j in range(c):
            new_row.append(new_matrix[k])
            k += 1
        reshaped_matrix.append(new_row)

    return reshaped_matrix


matrix = [[1,2],[3,4],[5,6]]
r = 2
c = 3

print(reshape(matrix, r, c))






class Matrix:
    def __init__(self,array):
        self.array = array
        self.len = len(array)

    def __str__(self):
        n = len(self.array)
        for i in range(n):
            for j in range(n):
                print(self.array[i][j],end='')
            print()
        return ''

    def flatten(self):
        res = []
        for i in range(len(self.array)):
            for j in range(len(self.array)):
                res.append(self.array[i][j])

        return res


    def convolution(self,other):
        n = len(self.array)
        k = other.len

        other = other.flatten()

        result = []


        for i in range(n - k + 1):
            new_row = []
            for j in range(n - k + 1):
                temp = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        temp.append(self.array[x][y])
                sum = 0
                for p in range(len(temp)):
                    sum += temp[p] * other[p]
                new_row.append(sum)
            result.append(new_row)


        return result







I = [[0,1,1,1,0,0,0],[0,0,1,1,1,0,0],[0,0,0,1,1,1,0],[0,0,0,1,1,0,0],[0,0,1,1,0,0,0,],[0,1,1,0,0,0,0],[1,1,0,0,0,0,0]]
K = [[1,0,1],[0,1,0],[1,0,1]]

I_matrix = Matrix(I)
K_matrix = Matrix(K)

print(I_matrix)
print("___________________")
print(K_matrix)
print("___________________")
convolution_matrix = Matrix(I_matrix.convolution(K_matrix))
print(convolution_matrix)



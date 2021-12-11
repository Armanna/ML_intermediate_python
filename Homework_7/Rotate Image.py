class Matrix:
    def __init__(self,array):
        self.array = array
        self.len = len(array)

    def __str__(self):
        n = self.len
        for i in range(n):
            for j in range(n):
                print(self.array[i][j]," ",end='')
            print()
        return ''

    def transpose(self):
        for i in range(self.len):
            for j in range(i, self.len):
                t = self.array[i][j]
                self.array[i][j] = self.array[j][i]
                self.array[j][i] = t

        return self

    def rotate(self):
        n = self.len
        a = 0
        b = 0
        c = 0
        d = 0

        for i in range(n // 2):             # 0
            for j in range(n - 2 * i - 1):  # 0 1
                a = self.array[i + j][i]
                b = self.array[n - 1 - i][i + j]
                c = self.array[n - 1 - i - j][n - 1 - i]
                d = self.array[i][n - 1 - i - j]

                self.array[i + j][i] = b
                self.array[n - 1 - i][i + j] = c
                self.array[n - 1 - i - j][n - 1 - i] = d
                self.array[i][n - 1 - i - j] = a


        return self


m = [[1,2,3],[4,5,6],[7,8,9]]
k = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

matrix_m = Matrix(m)
matrix_k = Matrix(k)


print(matrix_m)
print("_________________")
print(matrix_m.rotate())
print("-_-_-_-_-_-_-_-_-_-_-_")
print(matrix_k)
print("_________________")
print(matrix_k.rotate())



class Matrix:
    def __init__(self, *args, **kwargs):
        """
        Takes 2 keyword arguments: filename or list. If filename is given
        read the matrix from file. Else, read it directly from list.
        """
        if 'filename' in kwargs:
            self.read_from_file(kwargs['filename'])
        elif 'list' in kwargs:
            self.read_as_list(kwargs['list'])

    def read_as_list(self, matrix_list):
        if len(matrix_list) == 0:
            self._matrix = []
            self._columns = 0
            self._rows = 0
            return

        columns_count_0 = len(matrix_list[0])
        if not all(len(row) == columns_count_0 for row in matrix_list):
            raise ValueError('Got incorrect matrix')

        self._matrix = matrix_list
        self._rows = len(self._matrix)
        self._columns = columns_count_0

    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            matrix_list = f.readlines()
        matrix_list = list(map(lambda s: list(map(float, s[:-1].split(' '))), matrix_list))
        self.read_as_list(matrix_list)

    def __str__(self):
        s = '---------MATRIX---------\n'
        s += '\n'.join(str(row) for row in self._matrix)
        s += '\n'
        s += f'columns = {self.shape[0]}\nrows = {self.shape[1]}'
        s += '\n------------------------\n'
        return s

    def write_to_file(self, filename):
        """
        Write the matrix to the given filename.
        TODO: implement
        """
        f = open(filename, "w")
        [f.write(str(i)) for i in self._matrix]
        f.close()


    def transpose(self):
        """
        Transpose the matrix.
        TODO: implement
        """
        transpose_matrix = []
        for i in range(self._columns):
            new_row = []
            for j in range(self._rows):
                new_row.append(self._matrix[j][i])
            transpose_matrix.append(new_row)

        return transpose_matrix

    @property
    def shape(self):
        return self._rows, self._columns

    def __add__(self, other):
        """
        The `+` operator. Sum two matrices.
        TODO: implement
        """

        if isinstance(other, Matrix) and other.shape == self.shape:
            return [[(self._matrix[i][j] + other._matrix[i][j]) for j in range(self._columns)] for i in range(self._rows)]

        else:
            raise ValueError("an object of Matrix class cannot be added to an object other than Matrix, or shape mismatch")

    def __mul__(self, other):
        """
        The `*` operator. Element-wise matrix multiplication.
        Columns and rows sizes of two matrices should be the same.
        If other is not a matrix (int, float) multiply all elements of the matrix to other.
        TODO: implement
        """
        if isinstance(other, Matrix) and other.shape == self.shape:
            if isinstance(other, Matrix) and other.shape == self.shape:
                return [[(self._matrix[i][j] * other._matrix[i][j]) for j in range(self._columns)] for i in
                        range(self._rows)]

            else:
                raise ValueError(
                    "an object of Matrix class cannot be producted to an object other than Matrix, or shape mismatch")

        else:
            raise ValueError("an object of Matrix class cannot be added to an object other than Matrix, or shape mismatch")

    def __matmul__(self, other):
        """
        The `@` operator. Mathematical matrix multiplication.
        The number of columns in the first matrix must be equal to the number of rows in the second matrix.
        TODO: implement
        """

        if isinstance(other, Matrix) and self.shape[1] == other.shape[0]:

            new_matrix = []
            for i in range(self._rows): #{0,1}
                new_row = []
                for j in range(other._columns): #{0,1,2}
                    sum = 0
                    for k in range(other._rows): #{0,1,2}
                        sum += self._matrix[i][k] * other._matrix[k][j]
                    new_row.append(sum)
                new_matrix.append(new_row)

            return new_matrix

        else:
            raise ValueError(
                "an object of Matrix class cannot be dot producted to an object other than Matrix, or shape mismatch")


    @property
    def trace(self):
        """
        Find the trace of the matrix.
        TODO: implement
        """
        if self.shape[0] == self.shape[1]:
            sum = 0
            for i in range(self._rows):
                sum += self._matrix[i][i]

            return sum
        else:
            raise AttributeError("Non-square matrixes do not have traces")

    @property
    def determinant(self):
        """
        Check if the matrix is square, find the determinant.
        TODO: implement
        """
        if self.shape[0] == self.shape[1]:
            def reduced_matrix(matrix, a):
                new_matrix = []
                for i in range(1,len(matrix)):
                    new_row = []
                    for j in range(len(matrix[0])):
                        if j == a:
                            continue
                        new_row.append(matrix[i][j])
                    new_matrix.append(new_row)
                return new_matrix

            def determ(matrix):
                if len(matrix) == 2:
                    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
                return sum([(matrix[0][i] * (-1)**(0+i) * determ(reduced_matrix(matrix,i))) for i in range(len(matrix[0]))])

            return determ(self._matrix)

        else:
            raise AttributeError("Non-square matrixes do not have determinants")



matrix_1 = Matrix(list=[[1,2,3],[4,5,6]])
print("matrix_1:\n", matrix_1)
print("*******************************************************************************************")

matrix_2 = Matrix(list=[[4,5,6],[1,2,3]])
print("matrix_2\n:", matrix_2)
print("*******************************************************************************************")

matrix_1.write_to_file("text.txt")

print("The transpose of\n {m} is\n".format(m=matrix_1), matrix_1.transpose())
print("*******************************************************************************************")
print("The transpose of\n {m} is\n".format(m=matrix_2), matrix_2.transpose())
print("*******************************************************************************************")

print("The shape of\n {m} is\n".format(m=matrix_1), matrix_1.shape)
print("*******************************************************************************************")
print("The shape of\n {m} is\n".format(m=matrix_2), matrix_2.shape)
print("*******************************************************************************************")

print("{m_1}\n +\n {m_2}\n =\n".format(m_1=matrix_1, m_2=matrix_2), matrix_1 + matrix_2)
print("*******************************************************************************************")
print("{m_2}\n +\n {m_1}\n =\n".format(m_1=matrix_1, m_2=matrix_2), matrix_2 + matrix_1)
print("*******************************************************************************************")

print("{m_1}\n *\n {m_2}\n =\n".format(m_1=matrix_1, m_2=matrix_2), matrix_1 * matrix_2)
print("*******************************************************************************************")
print("{m_2}\n *\n {m_1}\n =\n".format(m_1=matrix_1, m_2=matrix_2), matrix_2 * matrix_1)
print("*******************************************************************************************")

matrix_3 = Matrix(list=matrix_2.transpose())

print("{m_1}\n @\n {m_3}\n =\n".format(m_1=matrix_1, m_3=matrix_3), matrix_1 @ matrix_3)
print("*******************************************************************************************")

matrix_4 = Matrix(list=matrix_1 @ matrix_3)
print("The trace of {m_4} is".format(m_4=matrix_4), matrix_4.trace)

matrix_5 = Matrix(list=[[7,4,2,0],[6,3,-1,2],[4,6,2,5],[8,2,-7,1]])
print("The determinant of\n {m_5} is\n".format(m_5=matrix_5), matrix_5.determinant)








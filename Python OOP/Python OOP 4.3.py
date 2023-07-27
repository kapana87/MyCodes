class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.data = [[value] * cols for _ in range(rows)]

    def get_value(self, rows, cols):
        return self.data[rows][cols]

    def set_value(self, rows, cols, value):
        self.data[rows][cols] = value

    def __str__(self):
        return "\n".join(" ".join(str(val) for val in row) for row in self.data)

    def __repr__(self):
        return f'{self.__class__.__name__}{self.rows, self.cols}'

    def __pos__(self):
        new_matrix = self.__class__(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.set_value(i, j, self.get_value(i, j))
        return new_matrix

    def __neg__(self):
        new_matrix = self.__class__(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.set_value(i, j, -self.get_value(i, j))
        return new_matrix

    def __invert__(self):
        new_matrix = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.set_value(j, i, self.get_value(i, j))
        return new_matrix

    def __round__(self, digits=None):
        new_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                value = self.get_value(i, j)
                new_value = round(value, digits) if digits is not None else round(value)
                new_matrix.set_value(i, j, new_value)
        return new_matrix



matrix = Matrix(2, 3, 1)

print(+matrix)
print()
print(-matrix)


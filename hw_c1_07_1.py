class Matrix:

    def __init__(self, inp_list):
        self.inp_list = inp_list

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, val)) for val in self.inp_list])

    def __add__(self, other):
        return Matrix(list(map(lambda x, y: list(map(lambda z, w: z + w, x, y)), self.inp_list, other.inp_list)))


ex = Matrix([[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]])
ex2 = Matrix([[4, 1, 2, 3], [3, 4, 1, 2], [2, 3, 4, 1], [1, 2, 3, 4]])
print(f'{ex} \n')
print(f'{ex2} \n')
print(f'Результат сложения матриц:\n{ex + ex2}\n')

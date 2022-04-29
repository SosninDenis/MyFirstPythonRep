class Cell:
    def __init__(self, numbs_in_cell):
        self.numbs_in_cell = numbs_in_cell

    def make_order(self, numbs_in_row):
        cell_with_row = ['*' * numbs_in_row] * (self.numbs_in_cell // numbs_in_row)
        if self.numbs_in_cell % numbs_in_row:
            cell_with_row.append('*' * (self.numbs_in_cell % numbs_in_row))
        return '\n'.join(cell_with_row)

    def __str__(self):
        return f'{self.numbs_in_cell}'

    def __add__(self, other):
        return Cell(self.numbs_in_cell + other.numbs_in_cell)

    def __sub__(self, other):
        assert self.numbs_in_cell > other.numbs_in_cell, 'Первая ячейка меньше второй'
        return Cell(self.numbs_in_cell - other.numbs_in_cell)

    def __mul__(self, other):
        return Cell(self.numbs_in_cell * other.numbs_in_cell)

    def __truediv__(self, other):
        return Cell(self.numbs_in_cell // other.numbs_in_cell)


a = Cell(15)
print(a.make_order(7))
b = Cell(13)
print(a+b)
print(a-b)
c = Cell(4)
d = Cell(3)
print(c*d)
print(c/d)
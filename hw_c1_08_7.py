# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
# работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.
class ComplexNumber:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    @staticmethod
    def split_number(number):
        new_number = []
        if '+' in number:
            new_number = number.split('+')
        elif '-' in number:
            new_number = number.split('-')
            if number[0] != '-':
                new_number[1] = '-' + new_number[1]
            else:
                new_number.pop(0)
                if len(new_number) > 1:
                    new_number[0] = '-' + new_number[0]
                    new_number[1] = '-' + new_number[1]
                else:
                    if 'i' in new_number[0]:
                        new_number[0] = '-' + new_number[0]
                        new_number = ['0'] + new_number
                    else:
                        new_number.insert(1, 0)
                        new_number[0] = '-' + new_number[0]
        else:
            if 'i' in number:
                new_number.append('0')
                new_number.append(number)
            else:
                new_number.append(number)
                new_number.append('0')
        for ind, el in enumerate(new_number):
            if 'i' in new_number[ind]:
                new_number[ind] = new_number[ind][:-1:]
        return list(map(int, new_number))

    def __add__(self, other):
        material_part = ComplexNumber.split_number(self.number)[0] + ComplexNumber.split_number(other.number)[0]
        imaginary_part = ComplexNumber.split_number(self.number)[1] + ComplexNumber.split_number(other.number)[1]
        if material_part == 0 and imaginary_part == 0:
            return ComplexNumber('0')
        elif material_part == 0 and imaginary_part != 0:
            return ComplexNumber(str(imaginary_part) + 'i')
        elif material_part != 0 and imaginary_part == 0:
            return ComplexNumber(str(material_part))
        elif imaginary_part > 0:
            return ComplexNumber(str(material_part) + '+' + str(imaginary_part) + 'i')
        else:
            return ComplexNumber(str(material_part) + str(imaginary_part) + 'i')

    def __mul__(self, other):
        x1, y1 = ComplexNumber.split_number(self.number)
        x2, y2 = ComplexNumber.split_number(other.number)
        material_part = x1 * x2 - y1 * y2
        imaginary_part = x1 * y2 + x2 * y1
        if material_part == 0 and imaginary_part == 0:
            return ComplexNumber('0')
        elif material_part == 0 and imaginary_part != 0:
            return ComplexNumber(str(imaginary_part) + 'i')
        elif material_part != 0 and imaginary_part == 0:
            return ComplexNumber(str(material_part))
        elif imaginary_part > 0:
            return ComplexNumber(str(material_part) + '+' + str(imaginary_part) + 'i')
        else:
            return ComplexNumber(str(material_part) + str(imaginary_part) + 'i')


a1 = ComplexNumber('1-12i')
a2 = ComplexNumber('-11+1i')
a3 = ComplexNumber('9+9i')
a4 = ComplexNumber('8i')
a5 = ComplexNumber('1')

print(a1 + a2)
print(a1 + a2 + a1 + a3 + a5)
print(a4 + a5)
print(a5 * a4)
print(a2 * a1)

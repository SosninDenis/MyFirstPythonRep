# Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

number_1 = input('Введите 1 число: ')
number_2 = input('Введите 2 число: ')
number_3 = input('Введите 3 число: ')


def my_func (arg_1, arg_2, arg_3):
    check_list = sorted([float(arg_1), float(arg_2), float(arg_3)], reverse=True)
    check_list.pop()
    return print(check_list[0] + check_list[1])


try:
    float(number_1)
    float(number_2)
    float(number_3)
    my_func(number_1, number_2, number_3)
except ValueError:
    print('Введенные числа не float')

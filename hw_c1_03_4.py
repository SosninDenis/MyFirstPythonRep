# Программа принимает действительное положительное число x и целое отрицательное число
# y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции
# my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения
# числа в степень

x = input('Введите число x = ')
y = input('Введите число y = ')


def check_numbers(x, y):
    try:
        if int(y) < 0 and x.isdigit():
            return True
    except ValueError:
        return False


def my_func(arg_1, arg_2):
    if check_numbers(arg_1, arg_2):
        arg_1 = int(arg_1)
        arg_2 = abs(int(arg_2))
        result = 1
        if abs(arg_2) == 1:
            return 1/arg_1
        if arg_2 != 1:
            for i in range(1, arg_2 + 1):
                result = result * 1/arg_1
            return result
    else:
        return 'Неверно были введены данные'


print(f'Результат = {my_func(x, y)}')

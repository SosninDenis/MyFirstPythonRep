# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.

number_1 = input('Введите делимое:')
number_2 = input('Введите делитель:')


def fun_division(arg_1, arg_2):
    return float(arg_1) / float(arg_2)


try:
    float(number_1)
    float(number_2)
    print(f'Результат деления = {fun_division(number_1, number_2)}')
except ValueError:
    print('Введенные числа не float')
except ZeroDivisionError:
    print('Ошибка - Деление на нуль')

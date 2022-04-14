# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
# платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
# время выполнения расчёта для конкретных значений необходимо запускать скрипт с
# параметрами.

from sys import argv


def salary_calculation(arg_1, arg_2, arg_3):
    try:
        float(arg_1)
        float(arg_2)
        float(arg_3)
        return float(arg_1) * float(arg_2) + float(arg_3)
    except:
        return 'Ошибка! Некорректные данные!'


print(f'Результат =  {salary_calculation(argv[1], argv[2], argv[3])}')

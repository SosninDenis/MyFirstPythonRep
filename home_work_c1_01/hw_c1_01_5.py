# Домашнее задание №1 Задача №5
# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
# финансовым результатом работает фирма. Например, прибыль — выручка больше издержек,
# или убыток — издержки больше выручки. Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение
# прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль
# фирмы в расчёте на одного сотрудника.

def ckeck (number):
    try:
        float(number)
        return True
    except:
        print('Вы ввели некорректный формат данных')

while True:
    revenue = input('Введите значение выручки: ')
    if ckeck(revenue):
        break
while True:
    costs = input('Введите значение издержки: ')
    if ckeck(costs):
        break
profit = float(revenue) - float(costs)
if profit > 0:
    print(f'Фирма работает с прибылью {profit}$')
    profitability = profit / float(revenue)
    print(f'Рентабельность фирмы {profitability:.2f}')
    while True:
        number_of_workes = input('Введите количество сотрудников в фирме: ')
        if (number_of_workes.isnumeric()):
            number_of_workes = int (number_of_workes)
            break
        else:
            print('Вы ввели неправильное количество сотрудников!')
    profit_per_worker = profit / number_of_workes
    print(f'Прибыль на одного сотрудника составляет - {profit_per_worker:.2f}$')
else:
    print('Фирма работает в убыток!')


# Домашнее задание №1 Задача №6
# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a
# километров. Каждый день спортсмен увеличивал результат на 10% относительно
# предыдущего. Требуется определить номер дня, на который результат спортсмена составит не
# менее b километров. Программа должна принимать значения параметров a и b и выводить
# одно натуральное число — номер дня.

def ckeck (number):
    try:
        float(number)
        return True
    except:
        print('Вы ввели некорректное значение дистанции')

while True:
    initial_value = input('Введите длинну дистанции для первого дня: ')
    if ckeck(initial_value):
        initial_value = float(initial_value)
        break
while True:
    final_value = input('Введите конечную длинну дистанции: ')
    if ckeck(final_value):
        final_value = float(final_value)
        break
i = 1
while True:
    i = i + 1
    initial_value = initial_value * 1.1
    if initial_value >= final_value:
        print(f'Необходимое количество дней для достижения результата: {i}')
        break

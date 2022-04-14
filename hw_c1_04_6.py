# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее


from itertools import count, cycle
from functools import reduce
import hw_c1_04_5


some_list = ['Повторяющийся', 'текст']
i = 0
while True:
    some_number = input('Введите начальное число: ')
    if some_number.isdigit():
        break
    print('Введено не целое число')
for el in count(int(some_number), 1):
    if reduce(hw_c1_04_5.my_func, [int(i) for i in str(el)]) > 20:
        break
    print(el)
for el in cycle(some_list):
    if i >= int(some_number):
        break
    print(el)
    i += 1

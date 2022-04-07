# Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
# сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
# input().

some_list = list()
number_of_list = 0
print('Вводите новые элементы.\nКогда закончите - введите "stop"')

while True:
    new_element = input(f'Введите элемент списка №{number_of_list}: ')
    if new_element == 'stop':
        break
    some_list.append(new_element)
    number_of_list += 1

if number_of_list <= 1:
    print('Упс! нечего переставлять!')
else:
    print(f'Получился список длиной {number_of_list} элементов: {some_list}')
    i = 0
    required_length = len(some_list) if len(some_list) % 2 == 0 else len(some_list) - 1

    while i < required_length:
        some_list[i], some_list[i+1] = some_list[i+1], some_list[i]
        i += 2

    print(f'Поменяли элементы местами и получилось: {some_list}')

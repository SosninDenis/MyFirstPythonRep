# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
# не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
# существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.

list_of_numbers = [7, 5, 3, 3, 3, 2, 2, 1]
print(f'Первоночальный список: {list_of_numbers}')
while True:
    new_element = input('введите новый элемент: ')
    if new_element.isdigit():
        new_element = int(new_element)
        break
for ind, el in enumerate(list_of_numbers):
    if new_element <= list_of_numbers[len(list_of_numbers) - 1]:
        list_of_numbers.insert(len(list_of_numbers), new_element)
        break
    elif new_element >= el:
        list_of_numbers.insert(ind, new_element)
        break
print(f'Новый список: {list_of_numbers}')

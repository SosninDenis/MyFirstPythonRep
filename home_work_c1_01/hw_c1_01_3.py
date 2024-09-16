# Домашнее задание №1 Задача №3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

while True:
    initial_number = input('Введите число: ')
    if initial_number.isnumeric():
        break
    else:
        print('Вы ввели некорректное число!')
i = 0
curent_number = ""
final_number = 0
while i < 3:
    curent_number += initial_number
    final_number += int(curent_number)
    i += 1
print(f'итоговый результат - {final_number}')
# Домашнее задание №1 Задача №4
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

while True:
    initial_number = input('Введите целое положительное число: ')
    if initial_number.isnumeric():
        break
    else:
        print('Вы ввели неположительное или не целое число!')
len_number = len(initial_number)
initial_number = int(initial_number)
max_number = 0
current_character = 0
while len_number > 0:
    current_character = initial_number // (10 ** (len_number - 1))
    if current_character > max_number:
        max_number = current_character
    initial_number = initial_number % (10 ** (len_number - 1))
    len_number -= 1
print(f'Самая большая цифра во веденном числе - {max_number}')


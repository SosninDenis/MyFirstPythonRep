# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран
from random import randint

with open('text_for_exercise_5.txt', 'w', encoding='utf-8') as file:
    for i in range(20):
        file.write(str(randint(1, 100)) + ' ')
with open('text_for_exercise_5.txt', 'r', encoding='utf-8') as file:
    gen = [int(ind) for ind in file.read().split()]
    print(f'Сумма чисел в файле равна {sum(gen)}')

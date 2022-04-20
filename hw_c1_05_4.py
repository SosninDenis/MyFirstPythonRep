# Создать (не программно) текстовый файл л со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл
dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре' }
with open('text_4.txt', 'r', encoding='utf-8') as file:
    with open('text_4_rus.txt', 'w', encoding='utf-8') as file2:
        for line in file:
            engl, *num = line.split()
            rus = dict[engl]
            file2.write(' '.join([rus] + num) + '\n')

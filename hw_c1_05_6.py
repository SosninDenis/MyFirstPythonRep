# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
# учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
# были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по
# нему. Вывести его на экран.
result = {}
number = 0
with open('text_6.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name_obj, list_num = line.split(':')
        list_num = list_num.split()
        for part in list_num:
            if '-' in part:
                continue
            numbers, _ = part.split('(')
            number += int(numbers)
        result[name_obj] = number
print(f'Итоговый словарь предметов {result}')

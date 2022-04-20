# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка
with open('exp_text.txt', 'w', encoding='utf-8') as file:
    while True:
        new_text = input('Введите новый текст ')
        file.write(new_text + '\n')
        if new_text and not new_text.isspace():
            continue
        else:
            break

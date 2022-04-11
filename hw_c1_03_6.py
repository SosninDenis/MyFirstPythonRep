# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
# возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых
# пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод
# исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте
# написанную ранее функцию int_func()


def int_func(arg):
    auxiliary_list = list(arg)
    auxiliary_list[0] = auxiliary_list[0].upper()
    result = ''
    for el in auxiliary_list:
        result += el
    return result


line_text = input('Введите строку слов из строчных букв: ').split()
result_line = []
for el in line_text:
    result_word = int_func(el)
    result_line.append(result_word)
main_result = result_line[0]
for ind in range(1, len(result_line)):
    main_result = main_result + ' ' + result_line[ind]
print(f'результат: "{main_result}" ')

#P.S. почему-то ментод ' 'join(result_line) не хотел склеивать с заглавными буками элементы списка через пробелы.
#Сами элементы в списке получались с заглавными буквами, как только делал склеивание - то первые закглавные буквы
#пропадали =( Шарил по инету - не нашел решения проблемы, поэтому так криво на ..кодил последнюю часть скрипта


# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке
with open('text_for_ex_2.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()
    print(content)
    print(f'В файле {len(content)} строк')
    for ind, val in enumerate(content, 1):
        print(f'В строке {ind} содержится - {len(val.split())} слов')

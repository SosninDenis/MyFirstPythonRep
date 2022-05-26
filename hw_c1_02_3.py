# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

list_of_season = ['зима', 'весна', 'лето', 'осень']
dict_of_season = {(1, 2, 12): 'зима', (3, 4, 5): 'весна', (6, 7, 8): 'лето', (9, 10, 11): 'осень'}
while True:
    user_month = input('введите целочисленный номер месяца: ')
    if user_month.isdigit() and int(user_month) < 13 and int(user_month) > 0:
        break
    print('Введен неправильный номер месяца!')

#Вариат решения задачки посредсом словаря
for el in dict_of_season.keys():
    for el1 in el:
        if el1 == int(user_month):
            print(f'месяц №{user_month} - это {dict_of_season.get(el)}')

#Вариант решения задачки посредставом списка
number_list = list(range(1, 13))
number_list.insert(0, number_list.pop(len(number_list)-1))
for ind, el in enumerate(number_list):
    if el == int(user_month):
        print(f'месяц №{user_month} - это {list_of_season[ind//3]}')

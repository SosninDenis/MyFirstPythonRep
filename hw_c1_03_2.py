# Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Осуществить вывод данных о
# пользователе одной строкой.

user_name = input('Введите имя пользователя: ')
user_surname = input('Введите фамилия пользователя: ')
user_year_of_birth = input('Введите год рождения: ')
user_city = input('Введите город проживания: ')
user_email = input('Введите email: ')
user_phonenumber = input('Введите номер телефона: ')


def print_fun(arg1, arg2, arg3, arg4, arg5, arg6):
    print(f'{arg1.capitalize()} {arg2.capitalize()}, {arg3} г.р., живёт в {arg4.capitalize()}, почта {arg5}, телефон {arg6}')


print_fun(user_name, user_surname, user_year_of_birth, user_city, user_email, user_phonenumber)

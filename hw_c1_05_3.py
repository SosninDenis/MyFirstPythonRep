# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.
with open('text_3.txt', 'r', encoding='utf-8') as file:
    average_income = 0
    numbers_of_users = 0
    for val in file:
        numbers_of_users += 1
        user_name, income = val.split()
        income = float(income)
        if income < 20000:
            print(f'Сотрудник {user_name} имеет оклад < 20000')
        average_income += income
    average_income /= numbers_of_users
    print(f'Cредняя величина дохода сотрудников равна {average_income}')

# Домашнее задание №1 Задача №2
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

initial_time = int(input('Введите количество секунд '))
time_hour = initial_time // 3600
time_minute = (initial_time % 3600) // 60
time_second = (initial_time % 3600) % 60
print(f'Введенное Вами время: {time_hour:02d}:{time_minute:02d}:{time_second:02d}')
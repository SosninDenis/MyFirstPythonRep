# Домашнее задание №1 Задача №2
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

while True:
    initial_time = input('Введите количество секунд: ')
    try:
        initial_time.isnumeric()
        initial_time = int(initial_time)
        break
    except:
        print('Вы ввели неправильный формат данных.')

time_hour = initial_time // 3600
time_minute = (initial_time % 3600) // 60
time_second = (initial_time % 3600) % 60
print(f'Введенное Вами время: {time_hour:02d}:{time_minute:02d}:{time_second:02d}')
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyOwnDivisionByZero(Exception):
    pass


divisible = int(input("Введите делимое: "))
divider = int(input("введите делитель: "))

try:
    if divider == 0:
        raise MyOwnDivisionByZero('Деление на ноль!')
except MyOwnDivisionByZero as err:
    print(err)
else:
    print(f'Результат деления {divisible} на {divider} равен {divisible / divider}')

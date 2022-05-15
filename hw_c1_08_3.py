# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на
# наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
# пользователя данные и заполнять список необходимо только числами. Класс-исключение
# должен контролировать типы данных элементов списка.


class CheckForPresenceText(Exception):

    @staticmethod
    def check_number(string_number):
        try:
            if float(string_number):
                return True
        except ValueError:
            return False


number_list = []
while True:
    current_number = input('Для заверешения ввода введите "stop"\nВведите новое число:')
    if current_number == 'stop':
        break
    try:
        if CheckForPresenceText.check_number(current_number):
            number_list.append(float(current_number))
        else:
            raise CheckForPresenceText('Введено не число!Введите число!')
    except CheckForPresenceText as err:
        print(err)
print(f'Итоговый список {number_list}')

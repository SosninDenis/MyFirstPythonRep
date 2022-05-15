# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.
class Time:
    day = 0
    month = 0
    year = 0

    def __init__(self, input_data):
        self.input_data = input_data

    @classmethod
    def conversion_method(cls, input_data):
        Time.is_valid_date(input_data)
        day, month, year = map(int, input_data.split('-'))
        return print(f'Из входных данных взвлечено: \nДень={day}\nМесяц={month}\nГод={year}')

    @staticmethod
    def is_valid_date(sting_data):
        flag = 0
        day, month, year = map(int, sting_data.split('-'))
        if month <= 12 and month >= 1:
            flag += 1
        if year >= 0:
            flag += 1
        if day >= 0 and day <= 29 and month == 2 and year % 4 == 0:
            flag += 1
        if day >= 0 and day <= 28 and month == 2 and year % 4 != 0:
            flag += 1
        if day >= 0 and day <= 31 and month in [1, 3, 5, 7, 8, 10, 12]:
            flag += 1
        if day >= 0 and day <= 30 and month in [4, 6, 9, 11]:
            flag += 1
        if flag >= 3:
            return print(f'{sting_data} - дата верна')
        else:
            return print(f'{sting_data} - дата неверна')


Time.is_valid_date('29-02-2000')
Time.is_valid_date('31-02-2000')
Time.is_valid_date('29-02-2001')
Time.is_valid_date('29-03-199')

example_date1 = Time.conversion_method('22-08-1989')







# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

from abc import ABC, abstractmethod


class OfficeWarehouse:
    all_equipment = []

    @classmethod
    def to_warehouse(cls, equipment):
        cls.all_equipment.append(equipment)
        print(equipment, 'Принято на склад.')

    def __str__(self):
        string = '\n'.join(map(str, self.all_equipment))
        return 'Устройства на складе:\n' + string if string else 'На складе нет устройств'


class Equipment(ABC):
    def __init__(self, brand, model, serial):
        self.brand = brand
        self.model = model
        self.serial = serial

    def __str__(self):
        return f'Оборудование {self.brand}, {self.model}, серийный номер {self.serial}'

    @abstractmethod
    def work(self):
        pass


class Printer(Equipment):
    def work(self):
        print(f'Принтер {self.brand}, {self.model} печатает')


class Scanner(Equipment):
    def work(self):
        print(f'Сканер {self.brand}, {self.model} печатает')


class Copier(Equipment):
    def work(self):
        print(f'Ксерокс {self.brand}, {self.model} копирует')


printer = Printer('Samsung', 'M2020', 123456)
scanner = Scanner('HP', 'M2020', 123456778)
copier = Copier('XEROX', 'M2020', 234123123)
OfficeWarehouse.to_warehouse(printer)
OfficeWarehouse.to_warehouse(scanner)
OfficeWarehouse.to_warehouse(copier)
print(OfficeWarehouse())

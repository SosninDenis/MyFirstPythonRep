# Реализовать класс Stationery (канцелярская принадлежность).
# ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ● в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return print('Starting rendering')


class Pen (Stationery):
    def draw(self):
        return print(f'Pen {self.title} starting rendering')


class Pencil (Stationery):
    def draw(self):
        return print(f'{self.title} starting rendering')


class Handle(Stationery):
    def draw(self):
        return print(f'Handle {self.title} starting rendering')


parker = Pen('Parker')
parker.draw()

simple_pencil = Pencil('Simple pencil')
simple_pencil.draw()

black_handle = Handle('black')
black_handle.draw()

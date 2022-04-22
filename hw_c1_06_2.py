# Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными;
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count_mass(self, weigth = 25, thicknes = 5):
        return print(float(self._width) * float(self._length) * weigth * thicknes / 1000)


ex = Road(20, 5000)
ex.count_mass()

ex2 = Road(100, 20)
ex2.count_mass(weigth=100, thicknes=10)

# Создать класс TrafficLight (светофор).
# - определить у него один атрибут color (цвет) и метод running (запуск);
# - атрибут реализовать как приватный;
# - в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# - продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# -переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# - проверить работу примера, создав экземпляр и вызвав описанный метод.
import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color  #initial color

    def running(self):
        some_list = ['red', 'yellow', 'green']
        dict = {'red': ['\033[31m', 7], 'green': ['\033[32m', 7], 'yellow': ['\033[33m', 2]}
        n = 0
        start_ind = some_list.index(self.__color)
        while True:
            if n == 0:
                for val in some_list[start_ind:]:
                    print(f'{dict[val][0]} {val}')
                    time.sleep(int(dict[val][1]))
            n = 1
            for val in some_list:
                print(f'{dict[val][0]} {val}')
                time.sleep(int(dict[val][1]))


ex = TrafficLight('green')
ex.running()

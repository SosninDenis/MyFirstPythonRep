# Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
class Car:
    is_police = False

    def __init__(self,speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        return print(f'{self.name} go')

    def stop(self):
        return print(f' {self.name} stop')

    def turn(self, durection):
        return print(f'{self.name} turn to the {durection}')

    def show_speed(self):
        return print(f'{self.name}`s speed is {self.speed}')


class SportCar(Car):
    pass


class TownCar(Car):
    def show_speed(self):
        print(f'{self.name}`s speed is {self.speed}')
        if self.speed > 60:
            return print(f'{self.name} exceeded the speed limit ')


class WorkCar(Car):
    def show_speed(self):
        print(f'{self.name}`s speed is {self.speed}')
        if self.speed > 40:
            return print(f'{self.name} exceeded the speed limit ')


class PoliceCar(Car):
    is_police = True


ex_sport_car = SportCar(100, 'red', 'Ferrari')
ex_sport_car.go()
ex_sport_car.turn('left')

ex_police_car = PoliceCar(200, 'black', 'WV Polo')
print(ex_police_car.is_police)
ex_police_car.show_speed()

ex_work_car = WorkCar(50,'red', 'Skoda')
ex_work_car.show_speed()

ex_town_car = TownCar(30, 'white', 'KIA')
ex_town_car.show_speed()
print(ex_town_car.is_police)

from abc import abstractmethod


class Clothes:
    all_clothes = 0

    def __init__(self, title):
        self.title = title
        Clothes.all_clothes += self.calculate_cloth

    @abstractmethod
    def calculate_cloth(self):
        pass


class Coats (Clothes):

    def __str__(self):
        return f'Пальто {self.title}, на него ушло {self.calculate_cloth:.02f} м2 ткани\n' \
               f'Общий расход ткани {Clothes.all_clothes:.02f} м2\n'

    def __init__(self, title, volume):
        self.volume = volume
        super().__init__(title)

    @property
    def calculate_cloth(self):
        return self.volume / 6.5 + 0.5


class Suits (Clothes):
    def __str__(self):
        return f'Костюм {self.title}, на него ушло {self.calculate_cloth:.02f} м2 ткани\n' \
               f'Общий расход ткани {Clothes.all_clothes:.02f} м2\n'

    def __init__(self, title, height):
        self.height = height
        super().__init__(title)

    @property
    def calculate_cloth(self):
        return self.height * 2 + 0.3


Coats_1 = Coats('Армани', 10)
print(Coats_1)
Suits_1 = Suits('Zara', 10)
print(Suits_1)
Suits_2 = Suits('АрмЯне', 2)
print(Suits_2)
Coats_2 = Coats('H&M', 30)
print(Coats_2)

class Clothes:
    class_clothes = 0
    all_clothes = 0
    def __init__(self):
        Clothes.all_clothes += self.class_clothes

    def calculate_all_cloth(self):
        print(f'{Clothes.all_clothes}')


class Coats (Clothes):

    def __init__(self, v):
        self.v = v
        self.class_clothes = self.v / 6.5 + 0.5
        super().__init__()

    def calculate_cloth(self):
        return self.class_clothes


class Suits (Clothes):
    def __init__(self, h):
        self.h = h
        self.class_clothes = self.h *2 + 0.3
        super().__init__()

    def calculate_cloth(self):
        return self.class_clothes

sd = Coats(6)
print(sd.calculate_cloth())
sf = Suits(13)
print(sf.calculate_cloth())
print(Clothes.all_clothes)

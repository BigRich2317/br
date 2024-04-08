
class Human():
    def __init__(self, health, mana, strength, dexterity):
        self.health = health
        self.mana = mana
        self.strength = strength
        self.dexterity = dexterity

class Paladin(Human):
    def info(self):
        print(f'Класс: Пладин')
        print(f'Здоровье: {self.health}')
        print(f'Мана: {self.mana}')
        print(f'Сила: {self.strength}')
        print(f'Ловкость: {self.dexterity}')

class Mercenary(Human):
    def info(self):
        print(f'Класс: Наёмник')
        print(f'Здоровье: {self.health}')
        print(f'Мана: {self.mana}')
        print(f'Сила: {self.strength}')
        print(f'Ловкость: {self.dexterity}')

p = Paladin(500, 300, 170, 60)
p.info()
m = Mercenary(500, 80, 170, 150)
m.info()
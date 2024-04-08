
class Human():
    def __init__(self, health, mana, strength, dexterity):
        self.health = health
        self.mana = mana
        self.strength = strength
        self.dexterity = dexterity

class Paladin(Human):
    def info(self):
        print(f'Здоровье: {self.health}')
        print(f'Мана: {self.mana}')
        print(f'Сила: {self.strength}')
        print(f'Ловкость: {self.dexterity}')
        
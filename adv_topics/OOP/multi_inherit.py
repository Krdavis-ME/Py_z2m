# Users
    # - Wizards
    # - Archers
    # - Different races


class User:
    def sign_in(self):
        print('logged in')
    
class Wizard(User):  # class ClassName(ParentClassName)
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'Attacking with the power of {self.power}')

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):                     # Method for checking arrows
        print (f'{self.arrows} remaining!')

    def run(self):
        print (f'Ran really fast')

class HybridBorg(Wizard, Archer):               # Inheriting from both wizard and archer
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hb1 = HybridBorg('Borgie', 50, 100)
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.sign_in())
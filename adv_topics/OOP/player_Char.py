#OOP- Creating a new object example

class PlayerCharacter:
    membership = True           # Class Oject Attribute - Static element
    def __init__(self, name, age):   # __init__ - a dunter Method, commonly called a construtor method
        self.name= name         # Properties or attributes of the object
        self.age = age
    
    def shout(self):
        print(f'My name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

        
player1 = PlayerCharacter('Mystic', 24) # Instantiating
player2 = PlayerCharacter('Nomad', 32)
player2.attack = 50
player3 = PlayerCharacter.adding_things(2,3)

print(player1.name)
print(player2.name)

print(player1.shout())
print(player2.shout())
print(player3.shout())

print(player3.age)
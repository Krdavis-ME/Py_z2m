#OOP
class NameOfClass():
    class_attribute = 'value'
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method(self):
        pass # code goes here

    @classmethod
    def cls_method_funct(cls, param1, param2):
        pass #code goes here

    @staticmethod
    def stc_method_funct(param1, param2):
        pass #code goes here
    

print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))

# Custom Objects
# class - keyword creates a new object
#       - use camel case when creating a new class
#       - Class -> Instantiate (creating a new instance,) -> Instances
class BigObject:    #New class; blueprinting
    pass

obj1 = BigObject()  # New object; Instantiating
print(type(obj1))

# Decorators
# functions are "First Class citizens"
#   - Can be used as arguments like a variable or a value

# Higher Order Function
#   - Can be a function that accepts a function as a parameter
#   - A function that returns another function

# Decorators add functionality to functions
 
# def hello():
#     print('Hello!')

def my_decorator(func):
    def wrap_func():
        print('*'*10)
        func()
        print('*'*10)
    return wrap_func

@my_decorator
def hello():
        print('Hello!')

hello()

# Calling Decorators in a Variable
hello2 = my_decorator(hello)
hello2()

# Calling Decorators as a function
my_decorator(hello)()
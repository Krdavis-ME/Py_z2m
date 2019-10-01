# Generators
# Creates values over time
# Example
#   range()

# def generator_function(num):
#     for i in range(num):
#         yield i

# for item in generator_function(1000):
#     print(item)

from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        time_start =time()
        result = func(*args, **kwargs)
        time_end = time()
        print(f'It took {time_end - time_start} s')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(1000000):
        i * 5

@performance
def long_time2():
    print('2')
    for i in list(range(1000000)):
        i * 5

long_time()
long_time2()
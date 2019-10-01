# Performance Decorator
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
    for i in range(1000000):
        i*5

long_time()
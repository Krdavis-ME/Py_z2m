# Fibonacci Numbers

def fib(number):                                # Function declaration for fibonacci sequence
    fib_first = 0                               # fib_first = declare the first value of the sequence
    fib_second = 1                              # fib_second = declare the second value of the sequence
    for i in range(number):                     # creating a range from the argument number, iterating over every value
        yield fib_first                         # Grabbing the first number
        fib_temp = fib_first                    # storing the first number temorarliy for calculation
        fib_first = fib_second                  # Setting fib_first to fib_second for calculation
        fib_second =  fib_temp + fib_second     # Calculating the Fibonocci sequence

for x in fib(20):                               # Iterating the function with the argument 20
    print(x)                                    # Printing results

# List form

# def fib2(number):
#     a = 0
#     b = 1
#     result = []
#     for i in range(number):
#         result.append(a)
#         temp = a
#         a = b
#         b = temp + b
#     return result

# print(fib2(100))
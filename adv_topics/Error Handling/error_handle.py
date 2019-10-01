# Error Handling

# Common errors
# - Syntax
# - Type Error
# - Undefined
# - Index out of range
# - Key/value error
# - Divide by zero

# try keyword
while True:
    try:
        age = int(input('What is your age? '))
        print(age)
        raise Exception('Hey cut it out!')
    except ValueError:
        print('Please enter a number! ')
    except ZeroDivisionError:
        print(f'Please enter an age greater than zero! ')
    else:
        print('Thank you!')
        break
    finally:
        print('Okay, I am finally done!')
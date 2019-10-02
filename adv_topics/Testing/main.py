

def do_stuff(num=0):
    try:
        if num:
            print(num)
            return int(num) +5
        else:
            print('Please Enter a Number')
    except ValueError as error:
        return error

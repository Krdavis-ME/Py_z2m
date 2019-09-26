# GUI exercise
# Given variable picture below, 
#   loop through variable, and display the zeros as blank spaces.
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]


for image in picture:
    for pixel in image:
        if (pixel ==1):
            print('*', end="")
        else:
            print(' ', end='')
    print('')
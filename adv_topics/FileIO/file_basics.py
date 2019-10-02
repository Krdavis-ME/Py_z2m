# File I/O 

# Opening a file
# open('file_name.txt')
#   - Can be assigned a variable name
#   my_file = open('file_name.txt')
#
# Closing the File
# my_file.close()

# Reading a file
# my_file.read()
#   - Can be printed out as well
#   - Can only be read once
# print(my_file.readline())
#   - Goes line by line in the file
# print(my_file.readlines())
#   - Provides a list of the lines

# Moving Index/cursor
# my_file.seek(0)

# Best Practices
# 
# with open('file_name.txt') as my_file:
#   print(my_file.readlines())

# MODE
# with open('file_name.txt', mode = 'r') as my_file:
#   - mode tells whether or not to read or right from the file
#   - default arg is 'r' for read
#   - 'w' is the arg for writing to the file
#       - Will create a file if it doesnt exist
#   - 'r+' allows to read and write
#   - 'a' appends to the end of the file

# Relative Paths & Absolute Paths
# 

# pathlib - Object-oriented filesystem 

# Error Handleing
# try:
#     with open('sad.txt', mode = 'r') as my_file:
#         print(my_file.read())
# except FileNotFoundError as err:
#     print('file does not exist')
#     raise err
# except IOError as err:
#   raise err
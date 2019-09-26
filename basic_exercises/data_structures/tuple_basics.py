# Tuple
# -immutable lists, like strings
# -allows for faster operation
my_tuble = (1,2,3,4,5)

new_tuble = my_tuble[1:2]
x,y,z, *other =(1,2,3,4,5)
print(new_tuble)

# Tuble Methods
# count(how often a value appears)
# .index
# len(tuple_name)
print(my_tuble.count(3))
print(my_tuble.index(2))
print(len(my_tuble))
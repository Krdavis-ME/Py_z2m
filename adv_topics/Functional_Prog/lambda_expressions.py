# Lamda Expressions
# replaces functions that have a singular use in the code
#
#  lamda parameter: function(parameter)/manipulation/action

from functools import reduce
# Map
my_list = [1,2,3]
def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, [1,2,3])))
print(list(map(lambda item: item*2, my_list)))
# Filter
def check_odd(item):
   return item % 2 != 0
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(list(filter(check_odd, my_list)))
print(my_list)

#Zip
your_list = [10,20,30]

print(list(zip(my_list, your_list)))

# Reduce
def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_list, 0))

# Lambda Squaring
their_list = [5,4,3]

print(list(map(lambda item: item ** 2, their_list)))

# Lambda Sorting
a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda num : num[1])
print(a)

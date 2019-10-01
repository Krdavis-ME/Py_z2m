# Pure functions
    # - Should receive same output with same inputs
    # - No side effects

# def multiply_by2(li):
#     new_list = []               #Local scope list
#     for item in li:
#         new_list.append(item*2)
#     return new_list

# print(multiply_by2([1,2,3]))

# Map, Filter, zip, and reduce
from functools import reduce
# Map
my_list = [1,2,3]
def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, [1,2,3])))

# Filter
def check_odd(item):
   return item % 2 != 0

print(list(filter(check_odd, my_list)))
print(my_list)

#Zip
your_list = [10,20,30]

print(list(zip(my_list, your_list)))

# Reduce
def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_list, 0))
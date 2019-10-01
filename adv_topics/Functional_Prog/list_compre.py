# List, Set and Dictionary Comprehension


# List Comprehension
# my_list = [param for param in iterable]

my_list = [char for char in 'hello']
my_list2 = [num for num in range(0,100)]
my_list3 = [num*2 for num in range(0,100)]
my_list4 = [num**2 for num in range(100) if num % 2 == 0]


print(my_list)
print('')
print(my_list2)
print ('')
print(my_list3)
print ('')
print(my_list4)

# Set Comprehension
my_set = {char for char in 'world'}

# Dictionary Comprehension
simple_dict = {
    'a':1,
    'b': 2
}
my_dict = {key: value**2 for key,value in simple_dict.items() }

print(my_dict)
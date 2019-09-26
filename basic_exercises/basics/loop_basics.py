# Loops
# -allow lines of code to run over and over

# FOR loops
# for VARIABLE in ITEM do something
#   - a variable is created for each value in item
a_list= [1,2,3,4,5,6]
for item in a_list:
    print(item)

# Iterable
# - list, dictionary, tuble, set, strings, range
# - Iterated -> one by one check each item in the collection
user = {
    'name': 'Golem',
    'age': 500,
    'can_swim': False
}
for item in user:
    print(item)
for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

# Counter
my_list = [1,2,3,4,5,6,7,8]

counter =0
for item in my_list:
    counter = counter + item
print (counter)

# Enumerate
# shows the index value
for i,char in enumerate('hellooo'):
    print(i, char)
for i,char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is: {i}')

# WHILE loops
# will keep looping until a condition is met

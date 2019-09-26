# Lists -Collections of items
#       - can hold any type of data
# 
# Li = [0,1,2,3,4]
# li = ['hand', 4, 'foot']

# List slicing
shopping_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

print(shopping_cart)

# Matrix
# is a nested list
matrix = [
    [1,2,3],
    [4,5,6]
    ]
print(matrix[0][1])

# Adding to list
# .insert(index, item)
# .extend([new_list])
# .append(item)
print(shopping_cart.append('laptop'))

# Removing from lists
# .pop(index value) - will return what was removed
# .remove(value to remove) - works 'in place'
# .clear()
basket = [1,2,3,4,5]
new_list = basket.pop(4)
print(new_list)

# Locating items
# .index(value, begining index value, ending index value)
# 'in' checks to see if value can be located
# 'not in'
bag = ['a','b','c','d','e']
print(bag.index('d',0,4))
print('d' in basket)

# Sorting
# .copy()
# .sort()
# .reverse()
# sorted(list_name)
old_basket = ['a','x','b','c','d','e']
new_basket = old_basket.copy()
old_basket.sort()

print(new_basket)
print(old_basket)

# tricks
# reversing a list
#   list_name[::-1]
# Creating a numerical list
#   list(range(1,100))
#   list(range(100))
# .join()
#   sentence = ' ' - and empty string
#   new_sentence = sentence.join(['hi', 'my', 'name', 'is'])

# List unpacking
# - Assigning variables to list values
a,b,c,*other, d = [1,2,3,4]
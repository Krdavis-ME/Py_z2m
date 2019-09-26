# Dictionary
# - an unordered collection of key-value pairs
# dictionary = { key: value}
#               ^ is called a key-value pair
# Example
dict_example = {'a':[1,2,3],
    'b':'hello',
    'c': True}

print(dict_example['c'])

# Keys
# - keys have to be immutable

# Common Methods
# .get - 'gets' the value of the key
dict_example1= {
    'basket': [1,2,3],
    'greet': 'hello'
}
print(dict_example1.get('greet'))
# if the Key doesnt exist, add a default value
print(dict_example1.get('age',55))

# creating a dictionary using the function
# dict(key=value)
dict_example2 = dict(name='MysticNomad')
print(dict_example2)
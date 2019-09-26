# Sets
# -Unordered collection of UNIQUE items
my_set = {1,2,3,4,5,6}
print(my_set)
my_set.add(100)
my_set.add(2)
print(my_set)

# Coverting Lists to Sets to reject duplicate values
my_list = ['a','b','c','d','d']
print(set(my_list))
# Checking for value in a Set
# -must search by the value in question
print('a' in my_list)

# Common Methods
# .difference() - finds the different values between two sets()
print(my_set.difference(set(my_list)))
# .discard()
# .difference_update() - updates the set to remove the simular values between two sets
# .intersection() -
#    shortcut for .intersection (set1 & set2)
# .isdisjoint() - Ask if two sets have the same values
# .union() - combines two sets, while removing non-unique values
#    shortcut for .union (set1 | set2)
# .issubset() - A subset is a set whos values are encompassed by another sets
# .issuperset()- A superset has values belong to a shorter set
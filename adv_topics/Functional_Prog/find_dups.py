# Print the duplicates from the list below as a list

some_list = ['a', 'b', 'c', 'b', 'd', 'm','n', 'n']

duplicates = list(set([value for value in some_list if some_list.count(value) > 1]))
print(duplicates)

# [value                            # Represents each value in the list
# for value in some_list            # Loops through each value in the list
# if some_list.count(value) > 1]    # counts the appearance of each value, adds them to the list

# set() - turned the duplicate list into a set, removing non unique answers
# list() - turned the set back into a list
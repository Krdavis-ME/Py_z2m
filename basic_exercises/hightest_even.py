# Given a list, print out the highest even number

# highest_even is a function, that has a parameter of a list
def highest_even(li):
    evens=[]    # a blank list that will be filled later
    for item in li: #iterating over the argument list
        if item %2 == 0:    # Checking the remainder of the numbers in the list
            evens.append(item) # if the number is even then it is added to the list evens
    return max(evens)   # returning the highest value in the evens list

print(highest_even([2,10,2,3,4,8,11]))
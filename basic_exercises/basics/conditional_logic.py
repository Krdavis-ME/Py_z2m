# Conditional Logic
# Keyword
#-----------------
# if  - condition evaluates to True
# is_old = False
# is_licenced =True

# if is_old:  # if is_old equals to True, print check check
#     print('check check')
# elif is_licenced:   # else if is_licenced equals to True, print 'oh no!'
#     print('oh no!')
# else:
#     print('hey hey')

# Truthy and Falsy
# Truthy - when a value is converted to boolean and evaluates to true
# 

# Ternary Operator
# - Conditional expression
# example
# is_friend = True
# can_message = "message allowed" if is_friend else "not allowed to message"
# print(can_message)

# Short Circuiting
#
# is_Friend = True
# is_user = True
# if is_Friend or is_user:
#     print('best friend forever')

#Logical operators
# -allows logical comparisons between two objects.

is_magician = True
is_expert = False

# Check if magician and expert : "you are a master magician"
#       if magician but not expert: "at least youre getting there"
#       of not magician: "you need magic powers"

if is_magician and is_expert:
    print('You are a master magician!')
elif is_magician and not is_expert:
    print("At least you're getting there!")
elif not is_magician:
    print("You need magicial powers!")

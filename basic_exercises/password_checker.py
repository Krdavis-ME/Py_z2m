# Creating a basic password checker
# 
# Username variable hold the user's name
username = input('What is your username? ')
# Receives password from user
password = input('what is your password? ')
password_length = len(password)
# Disquises the password
hidden_password = '*' * password_length
print(f'Hello {username}! Your password, {hidden_password}, is {password_length} characters long!')
# Password Validation

import re
# Password Conditions
# At least 8 chars long
# has to end with a number
# Contain any sort of letters numbers or $%#@


user_pass_check = re.compile(r"[A-Za-z0-9@#$%+=]{8,}")

user_password = 'DKRk9#@4'

check = user_pass_check.fullmatch(user_password)
print(check)
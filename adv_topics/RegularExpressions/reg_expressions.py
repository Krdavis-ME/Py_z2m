#Regular Expression
#
# not Python Specific

# Importing Regular Expression module
import re

pattern = re.compile('this')
string = 'search inside this string'

a = re.search('this', string)          #re.search return a 'match' object
print(a.span())                        # .span returns a tuble with the indices of the 'match' object
print(a.start())                       # .start returns the starting index of the object
print(a.end())                         # .end returns the ending index of the object 
print(a.group())                       # .group returns the value of the 'match' object

b = pattern.search(string)
c = pattern.findall(string)            # .findall returns every instance of the matched value
d = pattern.fullmatch(string)          # .fullmatch will only return a 'match' objects if the strings are exact.
e = pattern.match(string)


print(b)
print(c)

# Email Validation Example

# email_val = re.complie(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

# email = 'b@b.com'
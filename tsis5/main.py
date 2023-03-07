import re

# Program to match a string with 'a' followed by zero or more 'b's:

# string = input("Enter a string: ")

# if re.search(r'a[b]*', string):
#     print("Match found!")
# else:
#     print("Match not found.")

# # Program to match a string with 'a' followed by two to three 'b':

# string = input("Enter a string: ")

# if re.search(r'a[b]{2,3}', string):
#     print("Match found!")
# else:
#     print("Match not found.")

# # Program to find sequences of lowercase letters joined with an underscore:

# string = input("Enter a string: ")

# pattern = r'[a-z]+_[a-z]+'

# print(re.findall(pattern, string))

# # Program to find sequences of one upper case letter followed by lower case letters:


# string = input("Enter a string: ")

# pattern = r'[A-Z][a-z]+'

# print(re.findall(pattern, string))

# # Program to match a string that has an 'a' followed by anything, ending in 'b':


# string = input("Enter a string: ")

# if re.search(r'a.*b$', string):
#     print("Match found!")
# else:
#     print("Match not found.")


# Program to replace all occurrences of space, comma, or dot with a colon:

# string = input("Enter a string: ")

# pattern = r'[ ,.]'

# print(re.sub(pattern, ':', string))

# # Program to convert snake case string to camel case string:


# string = input("Enter a string in snake case: ")

# pattern = r'(_\w)'

# camel_case_string = re.sub(pattern, lambda x: x.group(1)[1].upper(), string)

# print("The camel case string is:", camel_case_string)


# # Program to split a string at uppercase letters:


# string = input("Enter a string: ")

# pattern = r'[A-Z][a-z]*'

# print(re.findall(pattern, string))


# # Program to insert spaces between words starting with capital letters:

# string = input("Enter a string: ")

# pattern = r'([A-Z][a-z]*)'

# spaced_string = re.sub(pattern, r' \1', string)

# print("The spaced string is:", spaced_string)


# # Program to convert a given camel case string to snake case:


# string = input("Enter a camel case string: ")

# pattern = r'([A-Z])'

# snake_case_string = re.sub(pattern, r'_\1', string).lower()

# print("The snake case string is:", snake_case_string)
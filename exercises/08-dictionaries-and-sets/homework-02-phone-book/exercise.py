# Homework 2: Phone book.
# You are building a phone book app. It stores each friend's name and phone
# number.
#
# 1. Write add_contact(book, name, number). It adds the contact, or updates
#    the number if the name exists. It returns nothing.
# 2. Write find_number(book, name). It returns the number, or "Unknown".
# 3. Write remove_contact(book, name). If the name is in the book, delete it
#    and return True. Otherwise return False.
# 4. (Advanced) Write names_starting_with(book, letter). It returns a list of
#    the names that start with letter.
#
# Expected input and output:
# book = {"Ana": "0151 111", "Ben": "0152 222"}
# find_number(book, "Zoe")              # returns 'Unknown'
# add_contact(book, "Zoe", "0153 333")
# find_number(book, "Zoe")              # returns '0153 333'
# remove_contact(book, "Ben")           # returns True
# remove_contact(book, "Ben")           # returns False
# names_starting_with(book, "Z")        # returns ['Zoe']
#
# Help:
# del book["Ana"]
# name = "Zoe"
# print(name[0])         # Z
#
# Write your solution below.

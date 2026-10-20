# Exercise 2 (advanced): Password checker
# Store each rule in a variable, then combine them with and.

username = input("Username: ")
password = input("Password: ")

long_enough = len(password) >= 8
no_123 = not password.startswith("123")
not_obvious = password.lower() != "password"
no_username = username.lower() not in password.lower()

strong = long_enough and no_123
strong = strong and not_obvious and no_username
print(strong)

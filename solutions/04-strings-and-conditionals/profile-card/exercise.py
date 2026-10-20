# Exercise 1: Profile card
# Ask for a name, city, and hobby, then print a short profile.

name = input("Name: ").strip().capitalize()
city = input("City: ").strip()
hobby = input("Hobby: ").strip()

print(f"Hi, my name is {name}.")
print(f"I live in {city}.")
print(f"I love {hobby}.")
print(f"My name has {len(name)} letters.")

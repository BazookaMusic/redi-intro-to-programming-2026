# Homework 7: Extended personal calculator
# Ask for two numbers and print all seven labeled arithmetic results.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", round(a / b, 2))
print("Remainder:", a % b)
print("Power:", a ** b)
print("Whole number division:", a // b)

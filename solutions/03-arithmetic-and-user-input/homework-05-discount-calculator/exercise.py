# Homework 5: Discount calculator
# Ask for a price and discount percentage, then print the final price.

price = float(input("Enter the price: "))
discount_percentage = float(input("Enter the discount percentage: "))

discount = price * discount_percentage / 100
final_price = round(price - discount, 2)
print("Final price:", final_price)

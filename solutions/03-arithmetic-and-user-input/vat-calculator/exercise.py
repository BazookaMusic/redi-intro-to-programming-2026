# VAT calculator
# Ask for a price, add 21% VAT, and print the total.

price = float(input("Enter a price (€): "))
total = round(price * 1.21, 2)
print("Price with VAT: €" + str(total))

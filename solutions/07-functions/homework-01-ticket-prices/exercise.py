def ticket_price(age):
    if age < 12:
        return 5
    return 10


child = ticket_price(8)
adult = ticket_price(16)
print(child)
print(adult)
print(child + adult)

# Solution for Exercise 3: Shopping basket
#
# total is created before the loop. If you created it inside the loop,
# it would go back to 0 each time.

prices = [4, 10, 3, 7]
total = 0

for price in prices:
    total = total + price
    print("Total so far:", total)

print("Final total:", total)

# Solution for Exercise 7: Times-table tower
#
# The heading is printed once for each table. The inner print() runs
# 5 times for each table, so 15 times in total.

for table in range(1, 4):
    print("Table of", table)
    for number in range(1, 6):
        print(table, "x", number, "=", table * number)

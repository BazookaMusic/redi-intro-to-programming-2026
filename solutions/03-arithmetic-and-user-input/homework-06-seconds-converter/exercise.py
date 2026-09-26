# Homework 6: Seconds converter
# Ask for seconds, then print full minutes and leftover seconds.

seconds = int(input("Enter the number of seconds: "))

minutes = seconds // 60
leftover_seconds = seconds % 60
print("Minutes:", minutes)
print("Seconds:", leftover_seconds)

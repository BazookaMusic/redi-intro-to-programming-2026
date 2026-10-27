# Homework 3: Count the long words
# Loop through the list and count how many words have more than 4 letters. Print the count.
#
# Example output:
# 3
#
# Write your solution below.
words = ["cat", "elephant", "dog", "tiger", "ox", "penguin"]

count = 0
for word in words:
    if len(word) > 4:
        count = count + 1
print(count)

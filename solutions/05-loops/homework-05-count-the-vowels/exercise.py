# Homework 5: Count the vowels
# Count the vowels in the word and print the count.

word = "programming"

count = 0
for letter in word:
    if letter in "aeiou":
        count = count + 1
print(count)

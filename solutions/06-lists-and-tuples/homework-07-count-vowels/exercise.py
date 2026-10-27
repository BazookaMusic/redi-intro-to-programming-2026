# Homework 7: Count vowels in a word
# Ask the user to type a word. Loop through each letter and count how many
# times each vowel (a, e, i, o, u) appears. Print the count for each vowel.
#
# Example input:
# programming
#
# Example output:
# a: 1
# e: 0
# i: 1
# o: 1
# u: 0
#
# Write your solution below.
word = input("Type a word: ")

vowels = ["a", "e", "i", "o", "u"]
for vowel in vowels:
    count = 0
    for letter in word:
        if letter == vowel:
            count = count + 1
    print(f"{vowel}: {count}")

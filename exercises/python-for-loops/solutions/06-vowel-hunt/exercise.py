# Solution for Exercise 6: Vowel hunt
#
# .lower() changes the uppercase I in ReDI to i, so it is counted too.

text = "Hello ReDI School"
count = 0

for letter in text:
    if letter.lower() in "aeiou":
        count = count + 1

print("Number of vowels:", count)

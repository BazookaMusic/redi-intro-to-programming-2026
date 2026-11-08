# Words for Hangman.
# Our Hangman game needs words that are not too long or too short.
# For this task, use a small list of words before connecting the library.
#
# 1. Write game_words(words). It returns a list containing only words with
#    4 to 8 letters, including both ends.
# 2. Print the result for ["cat", "apple", "banana", "watermelon"].
# 3. (Advanced) Write pick_word(words). It returns a random word from
#    game_words(words). Assume at least one word fits.
#
# Expected input and output:
# game_words(["cat", "apple", "banana", "watermelon"])
# returns ["apple", "banana"]
# pick_word(["cat", "apple", "banana"])
# returns "apple" or "banana"
# Your program prints: ['apple', 'banana']
#
# Help:
# result = []
# for word in words:
#     if 4 <= len(word) <= 8:
#         result.append(word)
#
# Write your solution below.

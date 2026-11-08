# Mini project: Hangman.
# Guess a secret eight-letter English word, one letter at a time.
# Correct guesses reveal letters. You can make six mistakes before losing.
# A skeleton moves towards the player after each mistake.
# Install english-words using the lesson README.
#
# 1. Write victory(word). It returns True if the displayed word has no _,
#    otherwise False.
# 2. Write display_hidden_word(secret_word, guessed_letters). It returns the word
#    with _ for each letter not yet guessed.
# 3. Write get_user_guess(guessed_letters). It asks for one letter from a to z
#    and returns it in lowercase. Ask again for invalid or repeated guesses.
#
# Expected input and output:
# display_hidden_word("linguist", ["i"])  # returns "_i___i__"
# victory("_i___i__")             # returns False
# victory("linguist")             # returns True
# get_user_guess(["i"])           # input " A " returns "a"; "i" asks again
# lives_bar(6, 6)                 # returns "💀______😊"
# lives_bar(6, 5)                 # returns "_💀_____😊"
# lives_bar(6, 0)                 # returns "______💀😊"
#
# Help:
# words = list(get_english_words_set(["web2"], lower=True))
# print(random.choice(words))
# for letter in secret_word:
#     if letter in guessed_letters:
#         print(letter)
# guess = input("Guess a letter: ").strip().lower()
#
# Write your solution below.

import random
from english_words import get_english_words_set


def victory(word):
    """Returns True when the displayed word has no hidden letters."""
    # ==================================================
    # >>> STEP 1: WRITE YOUR CODE HERE <<<
    # ==================================================
    pass


def display_hidden_word(secret_word, guessed_letters):
    """Returns underscores for letters that have not been guessed."""
    # ==================================================
    # >>> STEP 2: WRITE YOUR CODE HERE <<<
    # ==================================================
    pass


def get_user_guess(guessed_letters):
    """Asks until the player enters a new letter and returns it lowercase."""
    # ==================================================
    # >>> STEP 3: WRITE YOUR CODE HERE <<<
    # ==================================================
    pass


def hangman():
    secret_word = get_random_secret_word(8)
    total_lives = 6
    lives_left = total_lives
    guessed_letters = []

    while True:
        secret_word_display = display_hidden_word(secret_word, guessed_letters)
        print(secret_word_display)
        print(lives_bar(total_lives, lives_left))

        if victory(secret_word_display):
            print("You won!")
            return
        if lives_left == 0:
            print(f"You lost 💀 The word was {secret_word}.")
            return

        guess = get_user_guess(guessed_letters)
        guessed_letters.append(guess)
        if guess not in secret_word:
            print("Wrong guess!")
            lives_left -= 1
        else:
            print("Correct!")


# Supplied helpers.
def lives_bar(total_lives, lives_left):
    """Returns a skeleton moving towards the player after each mistake."""
    skeleton_position = total_lives - lives_left
    lives_display = ""
    for i in range(skeleton_position):
        lives_display += "_"
    lives_display += "💀"
    for i in range(total_lives - skeleton_position):
        lives_display += "_"
    lives_display += "😊"
    return lives_display


def get_random_secret_word(length):
    """Gets a random secret word of the requested length for our game."""
    web2lowerset = get_english_words_set(["web2"], lower=True)
    result = []
    for word in web2lowerset:
        if word.isascii() and word.isalpha() and len(word) == length:
            result.append(word)
    if not result:
        raise ValueError(f"No English words found with {length} letters.")
    return random.choice(result)


hangman()

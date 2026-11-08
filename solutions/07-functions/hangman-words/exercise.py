import random


def game_words(words):
    result = []
    for word in words:
        if 4 <= len(word) <= 8:
            result.append(word)
    return result


print(game_words(["cat", "apple", "banana", "watermelon"]))


def pick_word(words):
    return random.choice(game_words(words))

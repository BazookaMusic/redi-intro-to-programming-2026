def count_words(sentence):
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


print(count_words("the cat and the dog and the bird"))


def repeated_words(sentence):
    repeated = set()
    for word, count in count_words(sentence).items():
        if count > 1:
            repeated.add(word)
    return repeated


print(repeated_words("the cat and the dog and the bird"))

def count_votes(votes):
    counts = {}
    for vote in votes:
        counts[vote] = counts.get(vote, 0) + 1
    return counts


counts = count_votes(["zoo", "museum", "zoo", "park", "zoo", "park"])
print(counts)


def winner(counts):
    best_place = ""
    best_count = 0
    for place, count in counts.items():
        if count > best_count:
            best_place = place
            best_count = count
    return best_place


print(winner(counts))

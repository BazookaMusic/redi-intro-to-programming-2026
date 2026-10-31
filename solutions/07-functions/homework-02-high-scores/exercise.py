def count_high_scores(scores, minimum):
    count = 0
    for score in scores:
        if score >= minimum:
            count += 1
    return count


print(count_high_scores([12, 45, 7, 30], 20))

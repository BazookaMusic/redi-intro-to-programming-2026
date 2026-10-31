def average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)


result = average([12, 18, 24])
print(result)
if result >= 15:
    print("Pass")

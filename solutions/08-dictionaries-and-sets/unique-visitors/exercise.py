def unique_visitors(names):
    return len(set(names))


print(unique_visitors(["Ana", "Ben", "Ana", "Cleo", "Ben"]))


def first_visits(names):
    seen = set()
    result = []
    for name in names:
        if name not in seen:
            seen.add(name)
            result.append(name)
    return result


print(first_visits(["Ana", "Ben", "Ana", "Cleo", "Ben"]))

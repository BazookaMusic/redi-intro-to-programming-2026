def common_friends(friends1, friends2):
    return friends1.intersection(friends2)


def all_guests(friends1, friends2):
    return friends1.union(friends2)


ana_friends = {"Ben", "Cleo", "Dan"}
max_friends = {"Cleo", "Dan", "Eva"}
print(len(all_guests(ana_friends, max_friends)))


def everyone(groups):
    guests = set()
    for group in groups:
        guests = guests.union(group)
    return guests


print(len(everyone([{"Ben"}, {"Ben", "Cleo"}, {"Eva"}])))

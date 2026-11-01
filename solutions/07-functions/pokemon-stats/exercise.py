import pokebase


def total_stats(name):
    pokemon = pokebase.pokemon(name)
    total = 0
    for stat in pokemon.stats:
        total += stat.base_stat
    return total


print(total_stats("pikachu"))
print(total_stats("bulbasaur"))


def strongest(names):
    best = names[0]
    for name in names:
        if total_stats(name) > total_stats(best):
            best = name
    return best

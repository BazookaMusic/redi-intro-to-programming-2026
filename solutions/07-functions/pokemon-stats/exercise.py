import pokebase


pokemon = pokebase.pokemon("pikachu")
total = 0
for stat in pokemon.stats:
    total += stat.base_stat
print(total)

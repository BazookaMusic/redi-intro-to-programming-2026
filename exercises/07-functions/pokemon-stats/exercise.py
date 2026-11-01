# Pokemon stats.
# You are building a Pokedex app. Players want to know how strong each
# Pokemon is. A Pokemon's strength is the total of its six base stats.
# Install pokebase as explained in the lesson README.
#
# 1. Import pokebase. Write a function total_stats(name). It fetches the
#    Pokemon and returns the total of its six base stats.
# 2. Print the totals for Pikachu and Bulbasaur.
# 3. (Advanced) Write strongest(names). It takes a list of names and returns
#    the name with the highest total. Use total_stats inside it.
#
# Expected input and output:
# total_stats("pikachu")               # returns 320
# strongest(["bulbasaur", "pikachu"])  # returns "pikachu"
#
# Your program prints:
# 320
# 318
#
# Helpful code: each stat has a base_stat number.
# pokemon = pokebase.pokemon("pikachu")
# for stat in pokemon.stats:
#     print(stat.base_stat)  # 35, 55, 40, 50, 50, 90
#
# The real program needs internet access; check.py uses sample data offline.
#
# Write your solution below.

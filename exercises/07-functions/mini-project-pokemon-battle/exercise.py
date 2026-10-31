# Mini project: Pokemon battle.
# Install pokebase as explained in the lesson README.
# Implement get_hp(name): fetch the Pokemon with pokebase.pokemon(name)
# and return pokemon.stats[0].base_stat, its starting health.
# Implement attack(hp, damage): return hp minus damage, never below zero.
# Add a docstring to each function. Replace both pass placeholders.
# Fill the two missing attack() calls in the supplied loop.
# Enter any supported Pokemon name. Press Enter to attack.
# Damage is a random integer from 5 to 15. A defeated opponent cannot attack.
# The input and error-handling code is supplied; leave it unchanged.
#
# Sample input: pikachu, then Enter for each attack.
# One possible start of the output:
# Your Pokemon: pikachu
# You: pikachu (35 HP)
# Opponent: bulbasaur (45 HP)
# Press Enter to attack:
# bulbasaur has 33 HP.
# pikachu has 28 HP.
#
# Write your solution below.

import random
import pokebase


def get_hp(name):
    # Replace pass with your docstring and function body.
    pass


def attack(hp, damage):
    # Replace pass with your docstring and function body.
    pass


# Supplied setup: you do not need to learn exception handling for this task.
def choose_player():
    try:
        names = list(pokebase.APIResourceList("pokemon").names)
    except OSError as error:
        print(f"Could not load Pokemon data: {error}")
        raise SystemExit(1)
    while True:
        name = input("Your Pokemon: ").strip().lower()
        if not name:
            print("Please enter a Pokemon name.")
            continue
        if name not in names:
            print("Pokemon not found. Check the name and try again.")
            continue
        try:
            hp = get_hp(name)
        except OSError as error:
            print(f"Could not load Pokemon data: {error}")
            raise SystemExit(1)
        return name, hp


player_name, player_hp = choose_player()
opponent_name = random.choice(["pikachu", "bulbasaur", "charmander"])
try:
    opponent_hp = get_hp(opponent_name)
except OSError as error:
    print(f"Could not load opponent data: {error}")
    raise SystemExit(1)

print(f"You: {player_name} ({player_hp} HP)")
print(f"Opponent: {opponent_name} ({opponent_hp} HP)")

while player_hp > 0 and opponent_hp > 0:
    input("Press Enter to attack: ")
    damage = random.randint(5, 15)
    # Fill this gap: update opponent_hp by calling attack(opponent_hp, damage).
    print(f"{opponent_name} has {opponent_hp} HP.")

    if opponent_hp > 0:
        damage = random.randint(5, 15)
        # Fill this gap: update player_hp by calling attack(player_hp, damage).
        print(f"{player_name} has {player_hp} HP.")

if opponent_hp == 0:
    print("You win!")
else:
    print("You lose!")

# Mini project: Pokemon battle.
# You are building a battle game. You and the computer each pick a Pokemon
# and the program simulates the battle: they take turns hitting each other
# for random damage until one has 0 HP (health points).
# The starter below already runs the game. Install pokebase as explained in
# the lesson README.
#
# 1. Write get_hp(name). It fetches the Pokemon and returns its starting HP.
# 2. Write attack(hp, damage). It returns the HP left after the hit,
#    never below 0.
# 3. In the game loop, use attack to update opponent_hp and player_hp.
# 4. (Advanced) Write health_bar(hp). It returns one # for every full 10 HP.
#    Print it after each hit.
#
# Expected input and output:
# get_hp("pikachu")   # returns 35
# attack(35, 10)      # returns 25
# attack(5, 10)       # returns 0
# health_bar(35)      # returns "###"
#
# Helpful code: the first stat is HP.
# pokemon = pokebase.pokemon(name)
# print(pokemon.stats[0].base_stat)
#
# Write your solution below.

import random
import pokebase


def get_hp(name):
    # ==================================================
    # >>> STEP 1: WRITE YOUR CODE HERE <<<
    # ==================================================
    pass


def attack(hp, damage):
    # ==================================================
    # >>> STEP 2: WRITE YOUR CODE HERE <<<
    # ==================================================
    pass


# ==================================================
# >>> STEP 4 (ADVANCED): WRITE health_bar(hp) HERE <<<
# ==================================================


# The game
def main():
    player_name = choose_player()
    opponent_name = random.choice(["pikachu", "bulbasaur", "charmander"])
    player_hp = load_hp(player_name)
    opponent_hp = load_hp(opponent_name)

    print(f"You: {player_name} ({player_hp} HP)")
    print(f"Opponent: {opponent_name} ({opponent_hp} HP)")

    while player_hp > 0 and opponent_hp > 0:
        damage = random.randint(5, 15)
        # ==================================================
        # >>> STEP 3: UPDATE opponent_hp USING attack <<<
        # ==================================================
        print(f"{opponent_name} has {opponent_hp} HP.")

        if opponent_hp > 0:
            damage = random.randint(5, 15)
            # ==================================================
            # >>> STEP 3: UPDATE player_hp USING attack <<<
            # ==================================================
            print(f"{player_name} has {player_hp} HP.")

    if opponent_hp == 0:
        print("You win!")
    else:
        print("You lose!")


# Supplied helpers.
def load_names():
    try:
        return list(pokebase.APIResourceList("pokemon").names)
    except OSError as error:
        print(f"Could not load Pokemon data: {error}")
        raise SystemExit(1)


def load_hp(name):
    try:
        return get_hp(name)
    except OSError as error:
        print(f"Could not load Pokemon data: {error}")
        raise SystemExit(1)


def choose_player():
    names = load_names()
    while True:
        name = input("Your Pokemon: ").strip().lower()
        if name in names:
            return name
        print("Pokemon not found. Check the name and try again.")


main()

import random
import pokebase


def get_hp(name):
    """Fetch a Pokemon and return its starting health."""
    pokemon = pokebase.pokemon(name)
    return pokemon.stats[0].base_stat


def attack(hp, damage):
    """Return health after damage, with a minimum of zero."""
    remaining = hp - damage
    if remaining < 0:
        return 0
    return remaining


def health_bar(hp):
    """Return one # for every full 10 HP."""
    bar = ""
    for i in range(hp // 10):
        bar += "#"
    return bar


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
        opponent_hp = attack(opponent_hp, damage)
        print(f"{opponent_name} has {opponent_hp} HP.")
        print(health_bar(opponent_hp))

        if opponent_hp > 0:
            damage = random.randint(5, 15)
            player_hp = attack(player_hp, damage)
            print(f"{player_name} has {player_hp} HP.")
            print(health_bar(player_hp))

    if opponent_hp == 0:
        print("You win!")
    else:
        print("You lose!")


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

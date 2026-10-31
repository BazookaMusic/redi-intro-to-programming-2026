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
    opponent_hp = attack(opponent_hp, damage)
    print(f"{opponent_name} has {opponent_hp} HP.")

    if opponent_hp > 0:
        damage = random.randint(5, 15)
        player_hp = attack(player_hp, damage)
        print(f"{player_name} has {player_hp} HP.")

if opponent_hp == 0:
    print("You win!")
else:
    print("You lose!")

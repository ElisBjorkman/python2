import random


class Pokemon:
    def __init__(self, name : str, element : str, attack : int, defence : int, health : float ):
        self.name = name
        self.type = element
        self.attack = attack
        self.defence = defence
        self.health = health

def __str__(self):
    return f"{self.name,} {self.type}"


squirtle = Pokemon("Squirtle", "water", 90, 121, 198)
bulbasaur = Pokemon("Bulbasaur", "grass", 92, 92, 200)
charmander = Pokemon("Charmander", "fire", 98, 81, 188)
pikachu = Pokemon("Pikachu", "electric", 103, 76, 180)


def calculate_damage(atk_type, def_type, atk, deff):
    effect = 1

    if atk_type == "fire" and def_type == "grass":
        effect = 2
    elif atk_type == "fire" and def_type == "water":
        effect = 0.5
    elif atk_type == "fire" and def_type == "electric":
        effect = 1
    elif atk_type == "water" and def_type == "grass":
        effect = 0.5
    elif atk_type == "water" and def_type == "electric":
        effect = 0.5
    elif atk_type == "grass" and def_type == "electric":
        effect = 1

    return 50 * (atk/deff) * effect 

val = [Pokemon("Squirtle", "water", 90, 121, 198), Pokemon("Bulbasaur", "grass", 92, 92, 200), Pokemon("Charmander", "fire", 98, 81, 188), Pokemon("Pikachu", "electric", 103, 76, 180)]
lowest_health = 0

while True:
        print("Välj din Pokémon")
        for i in range(len(val)):
            print(i, val[i].name)

        player_input = int(input())

        player_pokemon = val[player_input]
        dator_pokemon = random.choice(val)

        spelare_max_health = player_pokemon.health
        dator_max_health = dator_pokemon.health

        

        dmg_taken = calculate_damage(player_pokemon.type, dator_pokemon.type, player_pokemon.attack,  dator_pokemon.defence)

        print(dmg_taken, "Skada")


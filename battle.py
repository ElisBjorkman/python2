
"""
fire > grass
fire < water
fire = electric
water < grass
water < electric
grass = electric


> 2x
= 1
< 0.5x

"""

import random


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

val = ["fire", "grass", "water", "electric"]
lowest_health = 0

while True:
        spelare_max_health = 200
        dator_max_health = 200

        while spelare_max_health > lowest_health and dator_max_health > lowest_health:
            dator_type1 = random.choice(val)
            spelare_type1 = input("what your type of pokemon:")
            print(f"datorn valde: {dator_type1}")

            dmg_taken = calculate_damage(spelare_type1, dator_type1, 30, 20)

            print(dmg_taken, "Skada")


            



from .i_weapon_behaviour import IWeaponBehaviour
import random


class DaggerBehaviour(IWeaponBehaviour):

    def calculate_damage(self, minimum):
        is_double_strike = random.randint(1, 100)

        if is_double_strike > 30:
            print("Double Strike!!!")
            return minimum * 2

        return minimum

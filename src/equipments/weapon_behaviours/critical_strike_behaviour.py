from .i_weapon_behaviour import IWeaponBehaviour
import random


class CriticalStrikeBehaviour(IWeaponBehaviour):

    def calculate_damage(self, minimum):
        is_critical_strike = random.randint(1, 100)

        if is_critical_strike > 70:
            print("Critical Strike!!!")
            return minimum * 3

        return minimum

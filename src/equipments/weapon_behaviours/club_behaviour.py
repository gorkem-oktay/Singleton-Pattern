from .i_weapon_behaviour import IWeaponBehaviour


class ClubBehaviour(IWeaponBehaviour):

    def calculate_damage(self, minimum):
        return minimum

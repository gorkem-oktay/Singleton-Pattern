from .i_weapon_behaviour import IWeaponBehaviour


class NormalHitBehaviour(IWeaponBehaviour):

    def calculate_damage(self, minimum):
        return minimum

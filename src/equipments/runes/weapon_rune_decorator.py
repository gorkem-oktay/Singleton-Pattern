from ..weapons.i_weapon import IWeapon


# Decorator interface
class WeaponRuneDecorator(IWeapon):

    def __init__(self, weapon):
        super().__init__()
        self.weapon = weapon

    def get_name(self):
        return self.weapon.get_name()

    def get_behaviour(self):
        return self.weapon.get_behaviour()

    def get_slot(self):
        return self.weapon.get_slot()

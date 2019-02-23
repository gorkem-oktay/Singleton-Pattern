from .weapon_rune_decorator import WeaponRuneDecorator


# Decorator concrete class
class DamageRune(WeaponRuneDecorator):

    def __init__(self, weapon):
        super().__init__(weapon)
        print("Added Damage Rune to " + self.get_name())

    def get_damage(self):
        return self.weapon.get_damage() + 2

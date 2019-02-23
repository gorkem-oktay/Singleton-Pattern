from .i_weapon import IWeapon
from ..i_equipment import EquipmentSlot
from ..weapon_behaviours.critical_strike_behaviour import CriticalStrikeBehaviour


class Sword(IWeapon):

    def __init__(self):
        super().__init__()
        self.set_name("Sword")
        self.set_damage(10)
        self.set_behaviour(CriticalStrikeBehaviour())
        self.set_slot(EquipmentSlot.RIGHT_HAND)

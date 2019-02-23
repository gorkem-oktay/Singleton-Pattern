from .i_weapon import IWeapon
from ..weapon_behaviours.dagger_behaviour import DaggerBehaviour
from ..i_equipment import EquipmentSlot


class Dagger(IWeapon):

    def __init__(self):
        super().__init__()
        self.set_name("Dagger")
        self.set_damage(4)
        self.set_behaviour(DaggerBehaviour())
        self.set_slot(EquipmentSlot.RIGHT_HAND)

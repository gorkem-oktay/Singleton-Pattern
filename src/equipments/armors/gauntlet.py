from .i_armor import IArmor
from ..i_equipment import EquipmentSlot


class Gauntlet(IArmor):

    def __init__(self):
        super().__init__()
        self.set_name("Gauntlet")
        self.set_slot(EquipmentSlot.HAND)
        self.set_protection(1)

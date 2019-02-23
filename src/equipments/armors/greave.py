from .i_armor import IArmor
from ..i_equipment import EquipmentSlot


class Greave(IArmor):

    def __init__(self):
        super().__init__()
        self.set_name("Greave")
        self.set_slot(EquipmentSlot.FOOT)
        self.set_protection(1)

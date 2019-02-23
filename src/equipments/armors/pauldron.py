from .i_armor import IArmor
from ..i_equipment import EquipmentSlot


class Pauldron(IArmor):

    def __init__(self):
        super().__init__()
        self.set_name("Pauldron")
        self.set_slot(EquipmentSlot.LEGS)
        self.set_protection(1)

from .i_armor import IArmor
from ..i_equipment import EquipmentSlot


class Cuirass(IArmor):

    def __init__(self):
        super().__init__()
        self.set_name("Cuirass")
        self.set_slot(EquipmentSlot.CHEST)
        self.set_protection(1)

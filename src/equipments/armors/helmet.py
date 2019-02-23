from .i_armor import IArmor
from ..i_equipment import EquipmentSlot


class Helmet(IArmor):

    def __init__(self):
        super().__init__()
        self.set_name("Helmet")
        self.set_slot(EquipmentSlot.HEAD)
        self.set_protection(1)

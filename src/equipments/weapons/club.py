from .i_weapon import IWeapon
from ..weapon_behaviours.club_behaviour import ClubBehaviour
from ..i_equipment import EquipmentSlot


class Club(IWeapon):

    def __init__(self):
        super().__init__()
        self.set_name("Club")
        self.set_damage(8)
        self.set_behaviour(ClubBehaviour())
        self.set_slot(EquipmentSlot.TWO_HAND)

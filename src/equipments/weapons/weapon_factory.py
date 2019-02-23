from ..i_equipment_factory import IEquipmentFactory
from .sword import Sword
from .dagger import Dagger
from .club import Club


class WeaponFactory(IEquipmentFactory):

    # Factory Method
    def get_equipment(self, name):
        if name == "Sword":
            return Sword()
        elif name == "Dagger":
            return Dagger()
        elif name == "Club":
            return Club()
        else:
            return None

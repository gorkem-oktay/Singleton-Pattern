from abc import ABC, abstractmethod
from equipments import EquipmentSlot


# Abstract Factory
class IEquipmentFactory(ABC):

    @abstractmethod
    def get_equipment(self, name):
        ...

    # Factory Method
    @staticmethod
    def get_factory(slot):
        from .weapons.weapon_factory import WeaponFactory
        from .armors.armor_factory import ArmorFactory

        if slot == EquipmentSlot.RIGHT_HAND or slot == EquipmentSlot.LEFT_HAND or slot == EquipmentSlot.TWO_HAND:
            return WeaponFactory()
        else:
            return ArmorFactory()

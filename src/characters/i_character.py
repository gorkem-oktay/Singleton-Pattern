from abc import ABC
from equipments.i_equipment_factory import IEquipmentFactory
from equipments.i_equipment import EquipmentSlot
from observables import Health


class ICharacter(ABC):

    def __init__(self):
        self.__name = "Unknown Name"
        self.__type = "Unknown Type"
        self.__health = None
        self.__equipments = {}

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_type(self, m_type):
        self.__type = m_type

    def get_type(self):
        return self.__type

    def set_health(self, health):
        if isinstance(health, Health):
            self.__health = health
        else:
            self.__health = Health(health)

    def get_health(self):
        return self.__health

    def equip(self, slot, name):
        """
        ICharacter doesn't know or care about the equipment itself.
        It doesn't need to know even if it is a weapon or an armor.
        It just gets the equipment and assigns it to corresponding slot.
        """
        factory = IEquipmentFactory.get_factory(slot)
        equipment = factory.get_equipment(name)

        if equipment.get_slot() != slot:
            print("Can't equip item to that slot")
            return

        if slot in self.__equipments:
            print("An item is already equipped in that slot")
        else:
            self.__equipments[slot] = equipment
            print(equipment.get_name() + " is equipped")

    def unequip(self, slot):
        self.__equipments.pop(slot)
        print("Item unequipped")

    def get_weapon(self):
        if EquipmentSlot.TWO_HAND in self.__equipments:
            return self.__equipments[EquipmentSlot.TWO_HAND]
        elif EquipmentSlot.RIGHT_HAND in self.__equipments:
            return self.__equipments[EquipmentSlot.RIGHT_HAND]
        else:
            return None

    def update_equipment(self, equipment):
        self.__equipments[equipment.get_slot()] = equipment

    def hit(self, to):
        weapon = self.get_weapon()

        if weapon is not None:
            damage = weapon.calculate_damage()
            to.get_health().decrease(damage)
        else:
            print("No equipped weapon")

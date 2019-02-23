from enum import Enum


class EquipmentSlot(Enum):
    RIGHT_HAND = 1
    LEFT_HAND = 2
    TWO_HAND = 3
    HEAD = 4
    CHEST = 5
    LEGS = 6
    HAND = 7
    FOOT = 8


class IEquipment:

    def __init__(self):
        self.__name = "Unknown Item"
        self.__slot = None

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_slot(self, slot):
        self.__slot = slot

    def get_slot(self):
        return self.__slot

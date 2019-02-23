from ..i_equipment import IEquipment


class IArmor(IEquipment):

    def __init__(self):
        super().__init__()
        self.__protection = 0

    def set_protection(self, value):
        self.__protection = value

    def get_protection(self):
        return self.__protection

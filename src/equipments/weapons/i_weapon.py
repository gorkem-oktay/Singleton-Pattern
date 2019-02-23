from ..i_equipment import IEquipment


class IWeapon(IEquipment):

    def __init__(self):
        super().__init__()
        self.__damage = 0
        self.__behaviour = None

    def set_damage(self, damage):
        self.__damage = damage

    def get_damage(self):
        return self.__damage

    def set_behaviour(self, behaviour):
        self.__behaviour = behaviour

    def get_behaviour(self):
        return self.__behaviour

    def calculate_damage(self):
        return self.get_behaviour().calculate_damage(self.get_damage())

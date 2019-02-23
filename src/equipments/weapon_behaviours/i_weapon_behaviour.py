from abc import ABC, abstractmethod


class IWeaponBehaviour(ABC):

    @abstractmethod
    def calculate_damage(self, minimum):
        ...

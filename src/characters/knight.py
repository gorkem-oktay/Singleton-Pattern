from characters import ICharacter
from observers import HealthBar


class Knight(ICharacter):

    def __init__(self):
        super().__init__()
        self.set_type("Knight")
        self.set_health(100)
        self.get_health().add_observer(HealthBar(self.get_type()))

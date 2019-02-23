from characters import ICharacter
from observers import HealthBar


class Troll(ICharacter):

    def __init__(self):
        super().__init__()
        self.set_type("Troll")
        self.set_health(140)
        self.get_health().add_observer(HealthBar(self.get_type()))

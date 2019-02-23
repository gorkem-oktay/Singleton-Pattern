from characters import ICharacter
from observers import HealthBar


class Goblin(ICharacter):

    def __init__(self):
        super().__init__()
        self.set_type("Goblin")
        self.set_health(60)
        self.get_health().add_observer(HealthBar(self.get_type()))

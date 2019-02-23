from characters import ICharacter
from observers import HealthBar


class Dummy(ICharacter):

    def __init__(self):
        super().__init__()
        self.set_type("Dummy")
        self.set_health(1000000)
        self.get_health().add_observer(HealthBar(self.get_type()))

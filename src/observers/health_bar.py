from observers import IObserver
from observables import Health


# Observer concrete class
class HealthBar(IObserver):

    def __init__(self, name):
        self.name = name

    def updated(self, observable, value):
        if isinstance(observable, Health):
            print(self.name + " received " + str(value) + " damage and " + str(observable.get_value()))

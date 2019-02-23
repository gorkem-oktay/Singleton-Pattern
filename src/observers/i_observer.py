from abc import ABC, abstractmethod


# Observer interface
class IObserver(ABC):

    @abstractmethod
    def updated(self, observable, value):
        ...

from abc import ABC


# Observable interface
class IObservable(ABC):

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def notify_all(self, value):
        for observer in self.__observers:
            observer.updated(self, value)

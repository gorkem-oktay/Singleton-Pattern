from observables import IObservable


# Observable concrete class
class Health(IObservable):

    def __init__(self, value):
        super().__init__()
        self.__value = value

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def decrease(self, value):
        self.__value -= value
        self.notify_all(value)

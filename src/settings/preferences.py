class Preferences:

    # Private instance
    __instance = None

    # Global access to singleton instance
    @staticmethod
    def get_instance():
        if Preferences.__instance is None:
            Preferences()

        return Preferences.__instance

    def __init__(self):
        # To prevent initialization of another instance so there is only one instance
        if Preferences.__instance is not None:
            raise Exception("Shouldn't have more than one instance!!")
        else:
            self.cache = {}
            Preferences.__instance = self

    def set(self, key, value):
        self.cache[key] = value

    def get(self, key):
        return self.cache[key]

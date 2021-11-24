# a singleton Handler of EVERYTHING


class Manager:
    def __init__(self, name) -> None:
        self.name = name

class SingletonManager(Manager):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not SingletonManager.__instance:
            SingletonManager.__instance = Manager(*args, **kwargs)
        return SingletonManager.__instance


sm = SingletonManager('Emasik')
sm = SingletonManager('Owl')

print(sm.name)


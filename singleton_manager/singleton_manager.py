# a singleton Handler of EVERYTHING


class Manager:
    def __init__(self, name) -> None:
        self.name = name

class MerveilleManager(Manager):
    __instance = None
    # another way to make it a singleton is to use Metaclass.
    def __new__(cls, *args, **kwargs):
        if not MerveilleManager.__instance:
            MerveilleManager.__instance = Manager(*args, **kwargs)
        return MerveilleManager.__instance


sm = MerveilleManager('Emasik')
sm = MerveilleManager('Owl')

print(sm.name)


# metaclass version

class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls._instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
            return cls._instance
        else:
            return cls._instance


class Merveille(metaclass=Singleton):
    def __init__(self, name) -> None:
        self.name = name


m = Merveille('Owl')
m = Merveille('Emasik')

print(m.name)

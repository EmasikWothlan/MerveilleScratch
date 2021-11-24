from types import MethodType


def foo(*args):
    print(args)


class Bar:
    name = 'bar'

    def set_method(self, mtd):
        self.method = MethodType(mtd, self)


b = Bar()
b.set_method(foo)
b.method()


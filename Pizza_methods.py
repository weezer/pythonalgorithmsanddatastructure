class Pizza(object):
    def __init__(self, size):
        self.size = size
        self.bbb = 666

    def gett_size(self):
        return self.size

    def retrun_num(self, num):
        return num


class Pizza2(Pizza):
    def __init__(self, size):
        super(Pizza2, self).__init__(size + 2)
        self.size = 123
        print str(self.bbb) + "Pizza2"


# print Pizza.gett_size(Pizza2(23))
# print Pizza2(123).gett_size.__self__

class PizaaWithStaticMethod(object):
    c = 123

    @staticmethod
    def static_Pizza(a, b):
        return a + b


print PizaaWithStaticMethod.static_Pizza(5, 6)


class PizzaFactory(object):
    c = 123

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def from_fridge(cls, fridge):
        print cls.c
        return cls(fridge.get_cheese() + fridge.get_vegetables())
class Custom(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __repr__(self):
        return '{} : {} {}'.format(self.__class__.__name__, self.name, self.number)

    def __cmp__(self, other):
        if hasattr(other, "getKey"):
            return self.getKey().__cmp__(other.getKey())

    def getKey(self):
        return self.number


class AnotherObject(object):
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number

    def __repr__(self):
        return '{} : {} {} {}'.format(self.__class__.__name__, self.name, self.age, self.number)

    def __cmp__(self, other):
        if hasattr(other, "getKey"):
            return self.getKey().__cmp__(other.getKey())

    def getKey(self):
        return self.age


def get_number(obj):
    return obj.number


if __name__ == "__main__":
    # print get_number(Custom("cao", 123))
    customlist = [
        Custom('object', 99),
        Custom('michael', 1),
        Custom('theodore the great', 59),
        Custom('life', 42)
    ]

    customlist2 = [
        Custom('object', 99),
        Custom('michael', 1),
        Custom('theodore the great', 59),
        Custom('life', 42),
        AnotherObject('bananas', 37, 2.2),
        AnotherObject('pants', 73, 5.6),
        AnotherObject('lemur', 44, 9.2)
    ]

    print sorted(customlist2)


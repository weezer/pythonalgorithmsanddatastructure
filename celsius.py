class Celsius:
    def __init__(self, temp = 0):
        self.set_temperature(temp)

    def to_farenhite(self):
        return self.get_temperature() * 1.8 + 32

    def get_temperature(self):
        return self._temp

    def set_temperature(self, temp):
        if temp < -237:
            raise ValueError("the celsius temp should not be lower than -237")
        self._temp = temp


class Celsius2:
    def __init__(self, temp = 0):
        self._temp = temp

    def to_farenhite(self):
        return self.temp * 1.8 + 32

    def get_temperature(self):
        print "get value"
        return self._temp

    def set_temperature(self, temp):
        if temp < -237:
            raise ValueError("the celsius temp should not be lower than -237")
        print "set value"
        self._temp = temp

    temp = property(get_temperature, set_temperature)

class Celsius3:
    def __init__(self, temp = 0):
        self._temp = temp

    def to_farenhite(self):
        return self.temp * 1.8 + 32

    @property
    def temp(self):
        print "get value"
        return self._temp

    @temp.setter
    def set_temperature(self, temp):
        if temp < -237:
            raise ValueError("the celsius temp should not be lower than -237")
        print "set value"
        self._temp = temp

if __name__ == "__main__":
    a = Celsius3(100)
    print a.to_farenhite()
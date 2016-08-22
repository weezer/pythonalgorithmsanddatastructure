from types import MethodType

def fn(self):
    return id(self), self, type(self)


class A_Class(object):
    def method_a(self):
        return id(self), self, type(self)


obja = A_Class()

setattr(A_Class, 'method_b', fn)

print obja.method_a()

print obja.method_b()



instance2 = A_Class()
setattr(obja, fn.__name__, MethodType(fn, obja, type(obja)))

# Calls the fn method attached to the instance
obja.fn()

# Throws an exception
instance2.fn()
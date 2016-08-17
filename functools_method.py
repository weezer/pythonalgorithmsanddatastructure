import functools


class MyClass(object):
    """demostration class for functools"""

    def meth1(self, a, b=2):
        """docstring for meth1()"""
        print '\tcalled meth1 with', (self, a, b)
        return

    def meth2(self, c, d=5):
        """docstring for meth2"""
        print '\tcalled meth2 with', (self, c, d)
        return

    wrapperd_meth2 = functools.partial(meth2, 'wrapped c')
    functools.update_wrapper(wrapperd_meth2, meth2)

    def __call__(self, e, f=6):
        """docstring for MyClass.__call__"""
        print '\tcalled object with:', (self, e, f)
        return


def show_details(name, f):
    """show details of a callable object."""
    print '%s:' % name
    print '\tobject:', f
    print '\t__name__:',
    try:
        print f.__name__
    except AttributeError:
        print '(no __name__)'
    print '\t__doc__', repr(f.__doc__)
    return

o = MyClass()

show_details('meth1 straight', o.meth1)
o.meth1('no default for a', b=3)
print

p1 = functools.partial(o.meth1, b=123)
functools.update_wrapper(p1, o.meth1)
show_details('meth1 wrapper', p1)
p1('a goes here')
print

show_details('meth2', o.meth2)
# o.wrapperd_meth2(123,234)
o.meth2('no default for c', d=666)
print

show_details('wrapped meth2', o.wrapperd_meth2)
o.wrapperd_meth2('no default for c', d=6)
print

show_details('instance', o)
o('no default for e')
print

p2 = functools.partial(o, f=7)
show_details('instance wrapper', p2)
p2('e goes here')
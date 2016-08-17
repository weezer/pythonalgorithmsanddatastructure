import functools


def myfunc(a, b=0):
    """this is a doc string of myfunc"""
    print "\t called my func with:", (a, b)
    return


def show_details(name, f, is_partial = False):
    """show details of a callable object"""
    print "%s:" % name
    print "\tobject", f
    if not is_partial:
        print "\t__name__", f.__name__
    print "\t__doc__", f.__doc__
    if is_partial:
        print '\tfunc', f.func
        print '\targs', f.args
        print '\tkeywords', f.keywords
    return

show_details("myfunc", myfunc)
myfunc('a', 3)
print

p1 = functools.partial(myfunc, b=4)
show_details('partial with myfunc', p1, True)
p1('default a')
p1('overide b', b=123)
print

p2 = functools.partial(myfunc, 'default a', b=100)
show_details('partial with a and b', p2, True)
p2()
p2(b='overide b')
print

p1()

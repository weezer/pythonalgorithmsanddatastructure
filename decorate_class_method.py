def dec_check(f):
  def deco(wrapper):
    print 'In deco'
    f(wrapper)
  return deco

class bar(object):
  @dec_check
  def foo(self):
    print 'in bar.foo'

b = bar()
b.foo()
from types import MethodType


class Person(object):
    def __init__(self, name):
        self.name = name


def play(self):
    print "%s is playing!" % self.name


p = Person('person')
p.play = MethodType(play, p)
p.play()
# print p.name
# pp = Person()
# pp.play()
pp = Person('haha')
pp.play = MethodType(play, pp, Person)
pp.play()

# Person.play = MethodType(play, None, Person)
# play = MethodType(play, None, Person)
# # print Person.__name__
# print type(Person.play)
# p3 = Person('p3')
# p3.play()

#
# Person.play = play
#
# p1 = Person('p1')
# p1.play()
#
# p2 = Person('p2')
# p2.play()

#setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.
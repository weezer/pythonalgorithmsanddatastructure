class OutCLass(object):
    @staticmethod
    def static1():
        print "outer static method"

    class InnerClass(object):
        def __init__(self):
            OutCLass.static1()


a = OutCLass()
a.InnerClass()
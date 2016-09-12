import functools

def my_decorator(func):
    def wrapper(name):
        return "after decorator: " + func(name)
    return wrapper

@my_decorator
def get_name(name):
    return "the name is " + name


def decorator_with_argument(arg):
    def arg_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return arg + " wrapper " + func(*args, **kwargs)
        return wrapper
    return arg_decorator


@decorator_with_argument("args")
def get_name2(name):
    """get name 2 docs"""
    return " 2 " + name


def decorator_change_parameter(func):
    def wrapper():
        return func("wrapper's value")
    return wrapper


@decorator_change_parameter
def get_name3(name):
    return "name 3 : " + name

print get_name("xxx")

print get_name2("aaa")
print get_name2.__name__
print get_name2.func_name
print get_name2.__doc__

print get_name3()
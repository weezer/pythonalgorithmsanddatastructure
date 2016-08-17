def my_decorator(func):
    def wrapper(*args, **kwargs):
        print 123
        return func(*args)
    return wrapper

@my_decorator
def my_func(num):
    print num


my_func('aa')

for i in range(1, 6):
    my_func(i)
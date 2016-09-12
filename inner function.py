def outer_function(outer_info):
    def inner_func(inner_info):
        return "outer: " + outer_info + " inner: " + inner_info

    return inner_func

first_out = outer_function("firt outer")
print first_out("first inner")
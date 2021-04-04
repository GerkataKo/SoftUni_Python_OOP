import functools


def type_check(type_data):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if type(*args, **kwargs) == type_data:
                return func(*args)
            return "Bad Type"

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))

import functools


def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args)
        return (f"you called {func.__name__}{args}\n"
                f"it returned {result}")
    return wrapper


@logged
def punk(*args):
    return 3 + len(args)


print(punk(4, 4, 4))

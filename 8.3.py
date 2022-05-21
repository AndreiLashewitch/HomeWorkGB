from functools import wraps


def logthis(fnc):
    @wraps(fnc)
    def wrapped(*args, **kwargs):
        print('log init value:', args[0])
        res = fnc(*args, **kwargs)
        print('log result:', res)
        return res

    return wrapped


@logthis
def your_func(your_arg):
    return your_arg + 10


print('your result:', your_func(10))
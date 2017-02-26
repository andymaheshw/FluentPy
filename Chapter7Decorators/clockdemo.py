import time


def clock(func):
    def clocked(*args):
        """
        Note for myself:

        args works here because it takes in a list/set,
        hence it doesn't matter what is in args. kwargs
        only takes in a dictionary or defined args.
        If you have (f, *kwargs), it will not like
        (1, 2, three=3) because *kwargs can't handle the two
        """
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked



def trace(func):
    def wrapper(*args):
        ret = func(*args)
        print('%s%r = %r' % (func.__name__, args, ret))
        return ret
    return wrapper

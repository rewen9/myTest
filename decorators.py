import functools
import time

def bench(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f'Time value = {end-start}')
        return return_value
    return wrapper

def dec_func(func):
    def caches(*args, **kwargs):
        y = 1525 ** func(*args, **kwargs)
        return y
    return caches


@bench
@dec_func
def xSqrt(x):
    return x**x+1


if __name__ == '__main__':
    # xSqrt.cache_clear()
    print(xSqrt(5))
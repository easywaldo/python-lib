import time
import functools


def elapsed_time(original_func):
    @functools.wraps(original_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print('함수 수행 시간: %f 초' % (end - start))
        return result
    
    return wrapper

@elapsed_time
def add(a, b):
    return a + b

result = add(3, 4)
    
print(add)
help(add)

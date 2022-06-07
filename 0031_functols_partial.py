def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result

print(add_mul('add', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(add_mul('mul', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

from functools import partial

add = partial(add_mul, 'add')
mul = partial(add_mul, 'mul')

print(add(1,2,3,4,5,6,7,8,9,10))
print(mul(1,2,3,4,5,6,7,8,9,10))

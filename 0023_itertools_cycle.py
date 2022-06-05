import itertools
employee_list = itertools.cycle(['waldo', 'jenny', 'evan', 'john', 'emma'])

# while True:
#     print(next(employee_list))


def repeat(object, times=None):
    # repeat(10, 3) --> 10 10 10
    if times is None:
        while True:
            print('a')
            print(object)
            yield object
    else:
        for i in range(times):
            print('b')
            yield object
result = list(map(pow, range(10), repeat(2)))
print(result)



result = list(map(pow, range(10), itertools.repeat(2)))
print(result)
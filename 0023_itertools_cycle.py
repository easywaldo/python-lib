import itertools
employee_list = itertools.cycle(['waldo', 'jenny', 'evan', 'john', 'emma'])

while True:
    print(next(employee_list))

import itertools

students = ['waldo', 'jenifer', 'rucia', 'beron', 'stella', 'mark', 'david']
rewards = ['candy', 'chcholate', 'jelly']

result = itertools.zip_longest(students, rewards, fillvalue='apple pie')
print(list(result))

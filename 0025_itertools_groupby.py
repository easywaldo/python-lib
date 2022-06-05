data = [
    {'name': '이민서', 'blood': 'O'},
    {'name': '이영순', 'blood': 'B'},
    {'name': '이상호', 'blood': 'AB'},
    {'name': '김지민', 'blood': 'B'},
    {'name': '최상현', 'blood': 'AB'},
    {'name': '김지아', 'blood': 'A'},
    {'name': '손우진', 'blood': 'A'},
    {'name': '박은주', 'blood': 'A'}
]

import operator
data = sorted(data, key=operator.itemgetter('blood'))

import pprint
pprint.pprint(data)

import itertools
grouped_data = itertools.groupby(data, key=operator.itemgetter('blood'))

result = {}
for key, value in grouped_data:
    result[key] = list(value)
    
pprint.pprint(result)
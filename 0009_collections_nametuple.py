from collections import namedtuple

data = [
    ('waldo', 42, 'python'),
    ('john', 31, 'kotlin'),
    ('gemma', 29, 'java')
]

Developer = namedtuple('Developer', 'name, age, language')
developer_list = [Developer(d[0], d[1], d[2]) for d in data]

print(developer_list)

d_list = [Developer._make(d) for d in data]
print(d_list)

print(f'{d_list[0].name}, {d_list[0].language}')

d1_dict = d_list[0]._asdict()
print(d1_dict)

new_d2 = d_list[1]._replace(language='csharp')
print(new_d2)

print(d_list[1])
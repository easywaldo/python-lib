import itertools

it = itertools.combinations(range(1, 46), 6)
print(it)

# for num in it:
#     print(num)

print(len(list(it)))
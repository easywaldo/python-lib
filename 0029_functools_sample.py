import functools

def xy_compare(n1, n2):
    if n1[1] > n2[1]:
        return 1
    elif n1[1] == n2[1]:
        if n1[0] > n2[0]:
            return 1
        elif n1[0] == n2[0]:
            return 0
        else:
            return -1
    else:
        return -1

src = [(0, 4), (-1, 4), (-2, 5), (1, 2), (1, -1), (2, 2), (3, 3)]
result = sorted(src, key=functools.cmp_to_key(xy_compare))
print(result)
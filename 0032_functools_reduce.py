import functools

data = [1,2,3,4,5,]
result = functools.reduce(lambda x,y: x + y, data)
print(result)

num_list = [12, 13, 6, 9, 10, 14, 21, 42, 5, 17]
max_num = functools.reduce(lambda x,y: x if x > y else y, num_list)
print(max_num)
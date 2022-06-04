import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)

print(result)

target = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(target)
print(target)
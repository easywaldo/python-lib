from collections import deque

a = [1,2,3,4,5]
q = deque(a)

print(a)
q.rotate(2)

result = list(q)
print(result)

b = [1,2,3,4,5]
q = deque(b)
q.rotate(-2)
result = list(q)
print(result)



c = [1,2,3,4,5]
q = deque(c)
q.append(6)

print(q)

q.appendleft(0)
num = q.pop()
print(num)

num = q.popleft()
print(num)

print(q)
import heapq

data = [
    (12.13, "foo"),
    (12.89, "bar"),
    (10.43, "alpha"),
    (11.35, "bravo"),
    (14.87, "charly"),
    (13.74, "delta")
]

h = []
for score in data:
    heapq.heappush(h, score)

for i in range(3):
    print(heapq.heappop(h))
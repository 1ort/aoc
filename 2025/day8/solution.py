from functools import reduce
import heapq
from collections import defaultdict
import operator

with open('input.txt') as f:
    points = [
        tuple(map(int, row.strip().split(','))) for row in f
    ]

def squared_dist(a: tuple[int, int, int], b: tuple[int, int, int]):
    x1, y1, z1 = a
    x2, y2, z2 = b
    return (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2

squared_distances = []

for i, point_a in enumerate(points):
    for point_b in points[i+1:]:
        heapq.heappush(
            squared_distances,
            (squared_dist(point_a, point_b), point_a, point_b)
        )

dsu = {point: point for point in points}

def dsu_find(point):
    while point != dsu[point]:
        dsu[point] = dsu[dsu[point]]
        point = dsu[point]
    return point

def dsu_union(a, b):
    parent_a, parent_b = dsu_find(a), dsu_find(b)
    if parent_a != parent_b:
        dsu[parent_a] = parent_b

def dsu_connected(a, b):
    return dsu_find(a) == dsu_find(b)


for i in range(1000):
    _, point_a, point_b = heapq.heappop(squared_distances)
    if dsu_connected(point_a, point_b):
        continue
    dsu_union(point_a, point_b)

dsu_circuits = defaultdict(set)
for elem in dsu:
    dsu_circuits[dsu_find(elem)].add(elem)

circuit_lens = sorted((len(circuit) for circuit in dsu_circuits.values()), reverse=True)

print('pt1:', reduce(operator.mul, circuit_lens[:3]))






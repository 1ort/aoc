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

class DSU:
    """disjoint set union""" 

    def __init__(self, points) -> None:
        self.dsu = {point: point for point in points}

    def find(self, point):
        while point != self.dsu[point]:
            self.dsu[point] = self.dsu[self.dsu[point]]
            point = self.dsu[point]
        return point

    def union(self, a, b):
        parent_a, parent_b = self.find(a), self.find(b)
        if parent_a != parent_b:
            self.dsu[parent_a] = parent_b

    def connected(self, a, b):
        return self.find(a) == self.find(b)
pt2_squared_distances = squared_distances.copy()

dsu = DSU(points)

for i in range(1000):
    _, point_a, point_b = heapq.heappop(squared_distances)
    if dsu.connected(point_a, point_b):
        continue
    dsu.union(point_a, point_b)

dsu_circuits = defaultdict(set)
for elem in dsu.dsu:
    dsu_circuits[dsu.find(elem)].add(elem)

circuit_lens = sorted((len(circuit) for circuit in dsu_circuits.values()), reverse=True)

print('pt1:', reduce(operator.mul, circuit_lens[:3]))

dsu = DSU(points)
while pt2_squared_distances:
    _, point_a, point_b = heapq.heappop(pt2_squared_distances)
    if dsu.connected(point_a, point_b):
        continue
    dsu.union(point_a, point_b)
    last_connected = (point_a, point_b)

print('pt2:', last_connected[0][0] * last_connected[1][0])





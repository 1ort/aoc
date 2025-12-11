from functools import cache


devices = {}

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        device = line.split(':')[0]
        connections = line.split()[1:]
        devices[device] = connections


count = 0

@cache
def count_paths(device) -> int:
    if device == 'out':
        return 1
    return sum(count_paths(conn) for conn in devices[device])

print('pt1:', count_paths('you'))




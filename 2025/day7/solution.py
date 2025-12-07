with open('input.txt') as f:
    rows = list(map(str.strip, f.readlines()))
beams = set()

total_splits = 0
total_timelines = 1


for row in rows:
    for i, ch in enumerate(row):
        if ch == 'S':
            beams.add(i)
            break
        if ch == '^' and i in beams:
            beams.remove(i)
            beams.add(i+1)
            beams.add(i-1)
            total_splits+=1

print('pt1:', total_splits)

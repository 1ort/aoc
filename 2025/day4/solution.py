positions = set()

with open('input.txt') as f:
    for y, row in enumerate(f.readlines()):
        for x, char in enumerate(row.strip()):
            if char == '@':
                positions.add((x, y))

max_coords = x, y

removable_rolls = set()
# pt 1
for x, y in positions:
    adjacent_rolls = 0
    for x_neig in (-1, 0, 1):
        for y_neig in (-1, 0, 1):
            if x_neig == y_neig == 0:
                continue
            if (x+x_neig, y+y_neig) in positions:
                adjacent_rolls += 1
    if adjacent_rolls < 4:
        removable_rolls.add((x, y))

print('pt1')
print(f'remove {len(removable_rolls)} rolls of paper')

print('pt2')
total_removed = len(removable_rolls)
#pt2 
while removable_rolls:
    positions.difference_update(removable_rolls)
    removable_rolls.clear()

    for x, y in positions:
        adjacent_rolls = 0
        for x_neig in (-1, 0, 1):
            for y_neig in (-1, 0, 1):
                if x_neig == y_neig == 0:
                    continue
                if (x+x_neig, y+y_neig) in positions:
                    adjacent_rolls += 1
        if adjacent_rolls < 4:
            removable_rolls.add((x, y))
    total_removed += len(removable_rolls)
    print(f'remove {len(removable_rolls)} rolls of paper')
print(f'total of {total_removed} rolls can be removed')


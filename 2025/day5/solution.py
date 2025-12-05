ranges = set()
ids = list()

with open('input.txt') as f:
    for line in f:
        if not line.strip():
            break  # to the ids loop
        begin, end = line.strip().split('-')
        ranges.add(range(int(begin), int(end)+1))

    for line in f:
        id_ = int(line.strip())
        ids.append(id_)

def is_fresh(ingridient):
    for range_ in ranges:
        if ingridient in range_:
            return True
    return False

fresh_ingridiends = 0
for id in ids:
    if is_fresh(id):
        fresh_ingridiends+=1

print(fresh_ingridiends)

def merge_ranges(a: range, b: range):
    if a.start > b.start:
        a, b = b, a

    if a.stop <= b.start:
        return None
    else:
        return range(a.start, max(a.stop, b.stop))

sorted_ranges = list(sorted(ranges, key=lambda range_: range_.start, reverse=True))
all_merged_ranges = list()


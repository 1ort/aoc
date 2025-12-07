intervals = set()
ids = list()

class Interval:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def __contains__(self, item) -> bool:
        if not isinstance(item, int):
            raise TypeError()
        return self.start <= item <= self.end

    def __hash__(self) -> int:
        return hash((self.start, self.end))

    def __repr__(self) -> str:
        return f"{self.start}-{self.end}"

    def __len__(self) -> int:
        return self.end - self.start + 1

with open('input.txt') as f:
    for line in f:
        if not line.strip():
            break  # to the ids loop
        begin, end = line.strip().split('-')
        intervals.add(Interval(int(begin), int(end)))

    for line in f:
        id_ = int(line.strip())
        ids.append(id_)

def is_fresh(ingridient):
    for interval in intervals:
        if ingridient in interval:
            return True
    return False

fresh_ingridiends = 0
for id in ids:
    if is_fresh(id):
        fresh_ingridiends+=1

print('pt1:',fresh_ingridiends)

def merge_two_intervals(a: Interval, b: Interval) -> Interval | None:
    if a.start > b.start:
        a, b = b, a
    if a.end < b.start:
        return None
    return Interval(a.start, max(a.end, b.end))

while True:
    # merge list of intervals until there are no possible merges left
    intervals = list(sorted(intervals, key=lambda i: i.start))
    start_size = len(intervals)
    merged_intervals = []
    interval_a = intervals.pop()
    while intervals:
        while True:
            interval_b = intervals.pop()
            merge_result = merge_two_intervals(interval_a, interval_b)
            if not merge_result:
                merged_intervals.append(interval_a)
                interval_a = interval_b
                break
            interval_a = merge_result
    merged_intervals.append(interval_a)
    intervals = merged_intervals
    if len(merged_intervals) == start_size:
        break

print('pt2:', sum(len(interval) for interval in intervals))

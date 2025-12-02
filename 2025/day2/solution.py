def is_invalid_id(id_: int) -> bool:
    x = str(id_)
    if len(x) % 2:
        return False
    return x[:len(x)//2] == x[len(x)//2:]


result = 0

with open('input.txt') as f:
    content = f.read()
    content.strip()
    ranges = content.split(',')
    for range_ in ranges:
        begin, end = range_.split('-')
        print(begin, end)
        for i in range(int(begin), int(end)+1):
            if is_invalid_id(i):
                result+=i
print(result)

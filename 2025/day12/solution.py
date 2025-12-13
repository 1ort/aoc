result = 0

with open('input.txt') as f:
    for i in range(30):
        f.readline()  # skip shapes

    for region in f:
        size = list(map(int, region.split(':')[0].split('x')))
        area = size[0] * size[1]

        shapes = list(map(int, region.strip().split()[1:]))

        if area >= 9 * sum(shapes):
            result += 1
print('pt1:', result)



def get_next_position(postition: int, direction: str, steps: int) -> int:
    if direction == 'L':
        steps = 100 - steps

    steps = steps % 100
    result = postition + steps
    return result % 100

    
def count_zero_clicks(pos: int, dir: str, steps: int) -> tuple[int, int]:
    zero_clicks = steps // 100
    steps = steps % 100

    if dir == 'L':
        if pos == 0:
            pos = 100
        if pos > steps:
            return pos - steps, zero_clicks
        else:
            return (100 + pos - steps) % 100, zero_clicks + 1
    else:
        if pos + steps < 100:
            return pos + steps, zero_clicks
        else:
            return (pos + steps - 100) % 100, zero_clicks + 1


# with open('input.txt') as f:
#     position = 50
#     password = 0
#     for line in f:
#         direction = line[0]
#         steps = int(line[1:])
#         position = get_next_position(position, direction, steps)
#         if position == 0:
#             password += 1
#         print(direction, steps, position)
#
#     print(password)

with open('input.txt') as f:
    position = 50
    zero_clicks_total = 0

    print(position)
    for line in f:
        direction = line[0]
        steps = int(line[1:])
        position, zero_clicks = count_zero_clicks(position, direction, steps)
        zero_clicks_total += zero_clicks
        print(f'{direction}{steps} -> {position}, {zero_clicks} zero_clicks')
    print(position, zero_clicks_total)



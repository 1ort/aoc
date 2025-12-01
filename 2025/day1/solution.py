def get_next_position(postition: int, direction: str, steps: int) -> int:
    if direction == 'L':
        steps = 100 - steps

    steps = steps % 100
    result = postition + steps
    return result % 100


with open('input.txt') as f:
    position = 50
    password = 0
    for line in f:
        direction = line[0]
        steps = int(line[1:])
        position = get_next_position(position, direction, steps)
        if position == 0:
            password += 1
        print(direction, steps, position)

    print(password)

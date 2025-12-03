def get_max_joltage(bank: list[int], batteries_left: int) -> int:
    max_pos = 0
    max_digit = 0

    for i in range(len(bank) - batteries_left):
        if bank[i] > max_digit:
            max_digit = bank[i]
            max_pos = i
    
    if batteries_left == 0:
        return max_digit
    else:
        return int(str(max_digit) + str(get_max_joltage(bank[max_pos+1:], batteries_left-1)))


total_joltage = 0
with open('input.txt') as f:
    for line in f:
        bank = [int(x) for x in line.strip()]

        max_joltage = get_max_joltage(bank, 11)
        total_joltage += max_joltage
        print(line, max_joltage)

print(total_joltage)

from functools import reduce
import re
from itertools import combinations
import operator

fewest_buttons = 0

with open('input.txt') as f:
    for line in f:
        indicator_light_diagram = re.findall(r'^\[(.+?)\]', line)[0]
        target_bits = int(indicator_light_diagram.replace('.', '0').replace('#', '1')[::-1], 2)
        button_wiring_schematics = [list(map(int, schem.split(',') )) for schem in re.findall(r'\((.+?)\)', line)] 
        button_wiring_bits  = []
        for button in button_wiring_schematics:
            button_bits = 0
            for bit in button:
                button_bits |= 1 << bit
            button_wiring_bits.append(button_bits)
        
        for i in range(1, len(button_wiring_bits)+1):
            for combination in combinations(button_wiring_bits, i):
                if reduce(operator.xor, combination) == target_bits:
                    fewest_buttons += i
                    break
            else:
                continue
            break

        print(bin(target_bits), [bin(button) for button in button_wiring_bits], i)

print('pt1:', fewest_buttons)

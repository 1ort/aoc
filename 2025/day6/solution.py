from functools import reduce
import operator


with open('input.txt') as f:
    raw_lines = f.readlines()

splitted_lines = [line.strip().split() for line in raw_lines]

grand_total = 0

for problem in zip(*splitted_lines):
    problem_result = reduce(operator.add if problem[-1] == '+' else operator.mul, map(int, problem[:-1]))
    grand_total += problem_result

print('part1:', grand_total)

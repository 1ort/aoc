from functools import reduce
import operator
import re

with open('input.txt') as f:
    raw_lines = f.readlines()

splitted_lines = [line.strip().split() for line in raw_lines]

grand_total = 0

for problem in zip(*splitted_lines):
    problem_result = reduce(operator.add if problem[-1] == '+' else operator.mul, map(int, problem[:-1]))
    grand_total += problem_result

print('part1:', grand_total)

operator_line = raw_lines.pop()
operator_line = operator_line.strip('\n') + ' '

splitted = re.split(r'\*|\+', operator_line)[1:]

lengths = list(map(len, splitted))

operators = operator_line.split()

offset = 0
all_problems = []
for op, max_len in zip(operators, lengths):
    raw_operands = [op] + [operands[offset:max_len+offset] for operands in raw_lines]
    offset += max_len + 1
    all_problems.append(raw_operands)

grand_total = 0
for problem in all_problems:
    op = problem[0]
    collums = [''.join(col).strip() for col in zip(*problem[1:])]
    problem_result = reduce(operator.add if op == '+' else operator.mul, map(int, collums))
    grand_total += problem_result

print('pt2:', grand_total)

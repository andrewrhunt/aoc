from math import prod
import re

with open("input.txt") as f:
    line = "".join([line for line in f])
    matches = [(prod(map(int, match.groups())), match.span()) for match in re.finditer(r'mul\((\d+),(\d+)\)', line)]
    ranges = [match.span() for match in re.finditer(r"don\'t\(\).*?do\(\)", line, re.DOTALL)]
    ans = [p for p, (b, e) in matches if not any(min < b < max for (min, max) in ranges)]
    print(sum(ans))
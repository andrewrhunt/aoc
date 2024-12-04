from math import prod
import re

with open(f"input.txt") as f:
    lines = [re.findall(r'mul\((\d+),(\d+)\)', line.strip()) for line in f]
    sum = sum([prod(map(int, tup)) for line in lines for tup in line])
    print(sum)

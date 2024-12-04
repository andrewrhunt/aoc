import re

def nums(s):
    return [int(match) for match in re.findall("(-?\d+)", s)]

with open("input.txt") as f:
    lines = [nums(line.strip()) for line in f]
    sa = sum([2*l[0]*l[1] + 2*l[1]*l[2] + 2*l[2]*l[0] for l in lines])
    slack = sum([sorted(l)[0]*sorted(l)[1] for l in lines])

print(sa+slack)
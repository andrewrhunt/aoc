with open(f"../input/d1p1.txt") as f:
    lines = [line.strip().split("   ") for line in f]
    lines = [int(loc) for line in lines for loc in line]
    a = sorted(lines[0::2])
    b = sorted(lines[1::2])
    total_dist = sum([abs(a-b) for a, b in zip(a, b)])

print(f"lines: {lines[:5]}")
print(f"a: {a[:5]}")
print(f"b: {b[:5]}")
print(f"total_dist: {total_dist}")

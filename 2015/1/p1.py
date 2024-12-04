with open("input.txt") as f:
    lines = f.read()

map = {
    "(": 1,
    ")": -1
}

print(sum([map[char] for char in lines]))
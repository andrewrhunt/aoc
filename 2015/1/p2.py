with open("input.txt") as f:
    lines = f.read()

map = {
    "(": 1,
    ")": -1
}

flr = 0
idx = 0 

while flr >= 0 and idx < len(lines):    
    flr += map[lines[idx]]
    idx += 1

print(idx)
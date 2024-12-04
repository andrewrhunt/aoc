with open(f"../input/d1p1.txt") as f:
    lines = [line.strip().split("   ") for line in f]
    lines = [int(loc) for line in lines for loc in line]
    a = sorted(lines[0::2])
    b = sorted(lines[1::2])

    a_uniq = set(a)
    occurences = {}
    for id in a_uniq:
        occurences[id] = 0

    for id in b:
        if id in occurences:
            occurences[id] += 1
    
    sim_score = 0
    for id in a:
        sim_score += id * occurences[id]
    
    print(f"Final Similarity Score: {sim_score}")

    


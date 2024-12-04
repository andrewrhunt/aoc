from typing import List

with open(f"input.txt") as f:
    lines = [line.strip().split(" ") for line in f]
    lines = [[int(loc) for loc in line] for line in lines]

    def is_safe(line: List[int]):

        diff = line[1] - line[0]
        if diff == 0:
            return False
        elif abs(diff) > 3:
            return False

        init_dir = diff / abs(diff) # +1 or -1

        index = 1

        while index < len(line)-1:
            cur = line[index]
            next = line[index + 1]
            diff = next - cur
            if diff == 0:
                return False
            elif abs(diff) > 3:
                return False
            dir = diff / abs(diff)
            if dir != init_dir:
                return False
            index += 1

        return True
    
    results = [is_safe(line) for line in lines]
    result_count = sum(results)

    print(f"Lines: {lines[0:5]}")
    print(f"Results: {results[0:5]}")
    print(f"Results: {result_count}")
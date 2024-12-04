from typing import Tuple, List

with open("input.txt") as f:
    grid = [[char for char in line.strip()] for line in f ]

    print(len(grid), len(grid[0]))

    dirs = {
        'n': (-1, 0),
        's': (1, 0),
        'e': (0, 1),
        'w': (0, -1),
        'ne': (-1, 1),
        'se': (1, 1),
        'nw': (-1, -1),
        'sw': (1, -1)
    }

    def search(seq: str, loc: Tuple[int, int], grid: List[List[str]], dir, x_max: int, y_max: int):

        x, y = loc
        
        print(seq, x, y, grid[x][y], dir, grid[x][y] == seq[0])

        if grid[x][y] == seq[0]:
            if len(seq) == 1:
                return True
            else:
                new_x, new_y = tuple(map(sum, zip(loc, dirs[dir])))
                if all([0 <= new_x <= x_max, 0 <= new_y <= y_max]):
                    return search(seq[1:], (new_x, new_y), grid, dir, x_max, y_max)
                else: 
                    return False
        else:
            return False

    print(dirs.items())

    ans = sum([search("XMAS", (i, j), grid, dir, len(grid[0])-1, len(grid)-1) for i, list in enumerate(grid) for j, char in enumerate(list) for dir, _ in dirs.items() if char == "X"])

    print(ans)



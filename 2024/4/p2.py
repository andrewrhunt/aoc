from typing import Tuple, List
from math import sqrt

with open("input.txt") as f:
    grid = [[char for char in line.strip()] for line in f ]

    def search(loc: Tuple[int, int], grid: List[List[str]], x_max: int, y_max: int):

        y, x = loc

        corners = [(y-1, x-1), (y-1, x+1), (y+1, x-1), (y+1, x+1)]

        # if corners not OOB
        if all([0 <= x <= x_max and 0 <= y <= y_max for y, x in corners]):
            return all([sorted([grid[n[0]][n[1]] for j, n in enumerate(corners) if i != j and sqrt((n[1]-c[1])**2 + (n[0]-c[0])**2) == 2]) == ["M", "S"] for i, c in enumerate(corners)])
        else: # corner oob, not MAS
            return False

    ans = sum([search((i, j), grid, len(grid[0])-1, len(grid)-1) for i, row in enumerate(grid) for j, col in enumerate(row) if col == "A"])

    print(ans)



grid = [[*row] for row in open(0).read().splitlines()]

def tilt(grid, d):
    if d == "N":
        for c in range(len(grid[0])):
            stop = 0
            for r in range(len(grid)):
                if grid[r][c] == '#':
                    stop = r + 1
                elif grid[r][c] == 'O':
                    grid[r][c] = '.'
                    grid[stop][c] = 'O'
                    stop += 1
    elif d == "S":
        for c in range(len(grid[0])):
            stop = len(grid) - 1
            for r in reversed(range(len(grid))):
                if grid[r][c] == '#':
                    stop = r - 1
                elif grid[r][c] == 'O':
                    grid[r][c] = '.'
                    grid[stop][c] = 'O'
                    stop -= 1
    elif d == "E":
        for r in range(len(grid)):
            stop = len(grid[0]) - 1
            for c in reversed(range(len(grid[0]))):
                if grid[r][c] == '#':
                    stop = c - 1
                elif grid[r][c] == 'O':
                    grid[r][c] = '.'
                    grid[r][stop] = 'O'
                    stop -= 1
    elif d == "W":
        for r in range(len(grid)):
            stop = 0
            for c in range(len(grid[0])):
                if grid[r][c] == '#':
                    stop = c + 1
                elif grid[r][c] == 'O':
                    grid[r][c] = '.'
                    grid[r][stop] = 'O'
                    stop += 1


directions = "NWSE"

visited = dict()
TOTAL = 1_000_000_000

for j in range(TOTAL):
    if str(grid) in visited:
        break

    visited[str(grid)] = j
    for i in range(4):
        tilt(grid, directions[i])

cycle_start = visited[str(grid)]
period = j - cycle_start

remaining = (TOTAL - cycle_start) % period

for _ in range(remaining):
    for i in range(4):
        tilt(grid, directions[i])

total = 0
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "O":
            total += len(grid) - r

print(total)

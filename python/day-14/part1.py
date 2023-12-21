grid = [[*row] for row in open(0).read().splitlines()]

total = 0
for c in range(len(grid[0])):
    stop = 0
    for r in range(len(grid)):
        if grid[r][c] == '#':
            stop = r + 1
        elif grid[r][c] == 'O':
            grid[r][c] = '.'
            grid[stop][c] = 'O'
            total += len(grid) - stop
            stop += 1


print(total)

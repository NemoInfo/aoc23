grid = open(0).read().strip().splitlines()
UNIVERSE_AGE = 1000000 - 1

positions = []
empty_cols = [True] * len(grid[0])
empty_rows = [True] * len(grid)

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "#":
            empty_rows[r] = False
            empty_cols[c] = False
            positions.append((r, c))

empty_rows = [i for i, b in enumerate(empty_rows) if b]
empty_cols = [i for i, b in enumerate(empty_cols) if b]

for er, empty_row in enumerate(empty_rows):
    for i in range(er + 1, len(empty_rows)):
        empty_rows[i] += UNIVERSE_AGE
    for i, (r, c) in enumerate(positions):
        if r < empty_row:
            continue
        positions[i] = (r + UNIVERSE_AGE, c)

for ec, empty_col in enumerate(empty_cols):
    for i in range(ec + 1, len(empty_cols)):
        empty_cols[i] += UNIVERSE_AGE
    for i, (r, c) in enumerate(positions):
        if c < empty_col:
            continue
        positions[i] = (r, c + UNIVERSE_AGE)

sum = 0
for i, (sr, sc) in enumerate(positions):
    for er, ec in positions[i+1:]:
        sum += abs(sr - er) + abs(sc - ec)

print(sum)

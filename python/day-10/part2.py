grid = open(0).read().strip().splitlines()

d = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
}

o = {
    "N": "S",
    "S": "N",
    "E": "W",
    "W": "E",
}

pipe = {
    ".": [],
    "|": ["N", "S"],
    "-": ["E", "W"],
    "L": ["N", "E"],
    "J": ["N", "W"],
    "7": ["S", "W"],
    "F": ["S", "E"],
    "S": ["N", "E", "S", "W"],
}

# Find S
for sr, row in enumerate(grid):
    for sc, ch in enumerate(row):
        if ch == "S":
            break
    else:
        continue
    break

loop = {(sr, sc)}
# Find a pipe that connects to S
r, c = sr, sc
for nd in pipe[grid[r][c]]:
    nr, nc = d[nd][0] + r, d[nd][1] + c
    if o[nd] in pipe[grid[nr][nc]]:
        r, c = nr, nc
        start_d = pd = nd
        break

# Find pipes part of loop
while grid[r][c] != "S":
    loop.add((r, c))
    for nd in pipe[grid[r][c]]:
        if o[nd] == pd:
            continue
        nr, nc = d[nd][0] + r, d[nd][1] + c
        r, c = nr, nc
        pd = nd
        break
end_d = pd

start_sym = [s for s, l in pipe.items() if o[end_d] in l and start_d in l][0]

n = len(grid) * 2 + 1
m = len(grid[0]) * 2 + 1
# Expand grid and filter junk
egrid = [["."] * m for n in range(n)]
for r in range(1, n, 2):
    for c in range(1, m, 2):
        sr = r // 2
        sc = c // 2
        if (sr, sc) in loop:
            if grid[sr][sc] == "S":
                egrid[r][c] = start_sym
            else:
                egrid[r][c] = grid[sr][sc]

print("\n".join(grid))
grid = egrid
# Connect horizontal
for r in range(1, n - 1):
    for c in range(2, m - 2, 2):
        if "E" in pipe[grid[r][c - 1]]:
            grid[r][c] = "-"

# Connect vertical
for r in range(2, n - 2, 2):
    for c in range(1, m - 1):
        if "N" in pipe[grid[r + 1][c]]:
            grid[r][c] = "|"

print("\n".join(["".join(row) for row in grid]))


# Flood
r, c = 0, 0
q = [(r, c)]
while len(q) > 0:
    r, c = q.pop()
    egrid[r][c] = "O"
    for dr, dc in d.values():
        nr, nc = r + dr, c + dc
        if not 0 <= nr < len(grid) or not 0 <= nc < len(grid[0]) \
           or egrid[nr][nc] != ".":
            continue
        q.append((r + dr, c + dc))

# Count inside
inside = 0
for i in range(1, len(grid), 2):
    for j in range(1, len(grid[0]), 2):
        if egrid[i][j] == ".":
            inside += 1

print(inside)

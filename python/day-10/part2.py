grid = open(0).read().splitlines()

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

def find_s():
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "S":
                return r, c

r, c = find_s()
loop = {(r, c)}
start_r, start_c = r, c
in_out = pipe[grid[r][c]]
for nd in in_out:
    nr, nc = d[nd][0] + r, d[nd][1] + c
    if o[nd] in pipe[grid[nr][nc]]:
        r, c = nr, nc
        pd = nd
        break
start_d = pd

while grid[r][c] != "S":
    loop.add((r, c))
    in_out = pipe[grid[r][c]]
    for nd in in_out:
        if o[nd] == pd:
            continue
        nr, nc = d[nd][0] + r, d[nd][1] + c
        if o[nd] in pipe[grid[nr][nc]]:
            r, c = nr, nc
            pd = nd
            break
end_d = pd

start_sym = [s for s, l in pipe.items() if o[end_d] in l and start_d in l][0]

n = len(grid) * 2 + 1
m = len(grid[0]) * 2 + 1

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


print("\n".join(["".join(row) for row in egrid]))
loop = set(map(lambda x: (x[0] * 2 + 1, x[1] * 2 + 1), loop))

for r in range(1, n - 1):
    for c in range(2, m - 2, 2):
        if "E" in pipe[egrid[r][c - 1]]:
            egrid[r][c] = "-"
            loop.add((r, c))

for r in range(2, n - 2, 2):
    for c in range(1, m - 1):
        if "N" in pipe[egrid[r + 1][c]]:
            egrid[r][c] = "|"
            loop.add((r, c))

grid = egrid
print("\n".join(["".join(row) for row in grid]))


outside = set()
def flood(r, c):
    if (r, c) in outside or (r, c) in loop:
        return
    q = [(r, c)]
    while len(q) > 0:
        r, c = q.pop()
        outside.add((r, c))
        for dr, dc in d.values():
            nr, nc = r + dr, c + dc
            if not 0 <= nr < len(grid) or not 0 <= nc < len(grid[0]) \
               or (nr, nc) in outside or (nr, nc) in loop:
                continue
            q.append((r + dr, c + dc))

left = [*zip(range(0, len(grid)), [0] * len(grid))]
right = [*zip(range(0, len(grid)), [len(grid[0]) - 1] * len(grid))]
top = [*zip([0] * len(grid[0]), range(0, len(grid[0])))]
bot = [*zip([len(grid) - 1] * len(grid[0]), range(0, len(grid[0])))]

border = [*left, *right, *bot, *top]
for r, c in border:
    flood(r, c)

inside  = set()
grid = [[*row] for row in grid]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) not in outside and (i, j) not in loop:
            grid[i][j] = "I"
            inside.add((i, j))
grid = ["".join(row) for row in grid]

print("\n".join(grid))

print(len(list(filter(lambda x: x[0] & 1 and x[1] & 1, inside))))

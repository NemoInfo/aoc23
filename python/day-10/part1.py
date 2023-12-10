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
in_out = pipe[grid[r][c]]
for nd in in_out:
    nr, nc = d[nd][0] + r, d[nd][1] + c
    if o[nd] in pipe[grid[nr][nc]]:
        r, c = nr, nc
        pd = nd
        break

count = 1
while grid[r][c] != "S":
    count += 1
    in_out = pipe[grid[r][c]]
    for nd in in_out:
        if o[nd] == pd:
            continue
        nr, nc = d[nd][0] + r, d[nd][1] + c
        if o[nd] in pipe[grid[nr][nc]]:
            r, c = nr, nc
            pd = nd
            break

print(count // 2)

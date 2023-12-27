grid = open(0).read().splitlines()

start = next((r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S")

def move(sources):
    new = set()
    for r, c in sources:
        for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
            if not (0 <= nr < len(grid) and
                    0 <= nc < len(grid[0])) or grid[nr][nc] == "#":
                continue

            new.add((nr, nc))
    return new

s = set([start])
for _ in range(64):
    s = move(s)

print(start, (len(grid), len(grid[0])))
print(len(s))

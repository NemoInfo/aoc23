grid = open(0).read().splitlines()
coords = set()

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch.isdigit() or ch == ".":
            continue

        for cr in [r - 1, r, r + 1]:
            for cc in [c - 1, c, c + 1]:
                if not 0 <= cr < len(grid) or not 0 <= cc < len(row) or not grid[cr][cc].isdigit():
                    continue

                while cc > 0 and grid[cr][cc - 1].isdigit():
                    cc -= 1

                coords.add((cr, cc))

s = 0
for r, cs in coords:
    ce = cs + 1
    while ce < len(grid[0]) and grid[r][ce].isdigit():
        ce += 1
    s += int(grid[r][cs:ce])

print(s)

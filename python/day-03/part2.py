grid = open(0).read().splitlines()
coords = set()

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch != "*":
            continue

        n = set()
        for cr in [r - 1, r, r + 1]:
            for cc in [c - 1, c, c + 1]:
                if not 0 <= cr < len(grid) or not 0 <= cc < len(row) or not grid[cr][cc].isdigit():
                    continue

                while cc > 0 and grid[cr][cc - 1].isdigit():
                    cc -= 1

                n.add((cr, cc))

        n = [*n]
        if len(n) == 2:
            coords.add((n[0], n[1]))


def number(r, cs):
    ce = cs + 1
    while ce < len(grid[0]) and grid[r][ce].isdigit():
        ce += 1
    return int(grid[r][cs:ce])


s = 0
for (a, b) in coords:
    s += number(*a) * number(*b)

print(s)

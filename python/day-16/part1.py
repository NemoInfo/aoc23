from collections import defaultdict
grid = open(0).read().splitlines()

stack = [((0, 0), (0, 1))]
visited = defaultdict(set)
while stack:
    (r, c), (dr, dc) = stack.pop()
    if (dr, dc) in visited[(r, c)]:
        continue
    if len(visited[(r, c)]) == 0:
        del visited[(r, c)]
    if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
        continue
    visited[(r, c)].add((dr, dc))
    if grid[r][c] == ".":
        stack.append(((r + dr, c + dc), (dr, dc)))
    elif grid[r][c] == "/":
        dr, dc = (-dc, -dr)
        stack.append(((r + dr, c + dc), (dr, dc)))
    elif grid[r][c] == "\\":
        dr, dc = (dc, dr)
        stack.append(((r + dr, c + dc), (dr, dc)))
    elif grid[r][c] == "|":
        if not dc:
            stack.append(((r + dr, c + dc), (dr, dc)))
            continue
        stack.append(((r + 1, c), (1, 0)))
        stack.append(((r - 1, c), (-1, 0)))
    elif grid[r][c] == "-":
        if not dr:
            stack.append(((r + dr, c + dc), (dr, dc)))
            continue
        stack.append(((r, c + 1), (0, 1)))
        stack.append(((r, c - 1), (0, -1)))

print(len(visited))

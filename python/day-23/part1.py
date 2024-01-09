grid = open(0).read().splitlines()

arrow = {
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0),
    "^": (-1, 0),
}

def dfs(pos, prev=None):
    if pos == (len(grid) - 1, len(grid[0]) - 2):
        return 0

    length = 0
    r, c = pos
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    valid_dirs = [d for d in dirs if 0 <= r + d[0] < len(grid) and
                  0 <= c + d[1] < len(grid[0]) and
                  grid[r + d[0]][c + d[1]] != "#" and
                  (r + d[0], c + d[1]) != prev]

    while len(valid_dirs) == 1:
        length += 1
        dr, dc = valid_dirs[0]
        prev = (r, c)
        r, c = r + dr, c + dc

        valid_dirs = [d for d in dirs if 0 <= r + d[0] < len(grid) and
                      0 <= c + d[1] < len(grid[0]) and
                      grid[r + d[0]][c + d[1]] != "#" and
                      (r + d[0], c + d[1]) != prev]


    if len(valid_dirs) == 0:
        if (r, c) == (len(grid) - 1, len(grid[0]) - 2):
            return length
        raise ValueError(f"Dead End at {r, c}")

    max_child = 0
    for dr, dc in valid_dirs:
        nr, nc = r + dr, c + dc
        if (dr, dc) != arrow[grid[nr][nc]]:
            continue
        max_child = max(max_child, 1 + dfs((nr, nc), (r, c)))

    return length + max_child

print(dfs((0, 1)))

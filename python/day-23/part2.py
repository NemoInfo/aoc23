from collections import deque, defaultdict

grid = open(0).read().splitlines()

graph = defaultdict(dict)

end = (len(grid) - 1, len(grid[0]) - 2)
queue = deque([(0, 1, 1, 0)])
visited = set()
while queue:
    nr, nc, dr, dc = queue.popleft()
    visited.add((nr, nc, dr, dc))
    pr, pc = nr, nc
    cr, cc = nr + dr, nc + dc

    length = 1
    dirs = [
        (dr, dc) for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)] if
        0 <= cr + dr < len(grid) and
        0 <= cc + dc < len(grid[0]) and
        grid[cr + dr][cc + dc] != "#" and
        (cr + dr, cc + dc) != (pr, pc)
    ]

    while len(dirs) == 1:
        length += 1
        dr, dc = dirs[0]
        pr, pc = cr, cc
        cr, cc = cr + dr, cc + dc

        dirs = [
            (dr, dc) for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)] if
            0 <= cr + dr < len(grid) and
            0 <= cc + dc < len(grid[0]) and
            grid[cr + dr][cc + dc] != "#" and
            (cr + dr, cc + dc) != (pr, pc)
        ]

    if len(dirs) == 0:
        if (cr, cc) == end:
            graph[(nr, nc)][(cr, cc)] = length
            graph[(cr, cc)][(nr, nc)] = length
        continue

    graph[(nr, nc)][(cr, cc)] = length
    graph[(cr, cc)][(nr, nc)] = length
    for dr, dc in dirs:
        if (cr, cc, dr, dc) not in visited:
            queue.append((cr, cc, dr, dc))

graph = dict(graph)

def find_max_cost_path(start, end, visited=None, path_cost=0, max_cost=0, max_path=None):
    if visited is None:
        visited = set()
    if max_path is None:
        max_path = []

    visited.add(start)

    if start == end:
        if path_cost > max_cost:
            max_cost = path_cost
            max_path = list(visited)
    else:
        for neighbor in graph[start]:
            if neighbor in visited:
                continue
            new_cost = path_cost + graph[start][neighbor]

            new_max_cost, new_max_path = find_max_cost_path(neighbor, end, visited.copy(), new_cost, max_cost, max_path)
            if new_max_cost > max_cost:
                max_cost = new_max_cost
                max_path = new_max_path

    return max_cost, max_path

max_cost, max_path = find_max_cost_path((0, 1), end)

print(max_cost, max_path)

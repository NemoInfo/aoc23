from heapq import heappop, heappush

grid = [[*map(int, row.strip())] for row in open(0)]

visited = set()
queue = [(grid[0][1], (0, 1), (0, 1), 1), (grid[1][0], (1, 0), (1, 0), 1)]
while queue:
    cost, (r, c), (dr, dc), t = heappop(queue)

    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        print(cost)
        break

    if ((r, c), (dr, dc), t) in visited:
        continue

    visited.add(((r, c), (dr, dc), t))

    nr, nc = r + dr, c + dc
    if t < 3 and 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
        heappush(queue, (cost + grid[nr][nc], (nr, nc), (dr, dc), t + 1))

    # Turn left
    ld = complex(dr, dc) * 1j
    ldr, ldc = int(ld.real), int(ld.imag)
    nr, nc = r + ldr, c + ldc
    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
        heappush(queue, (cost + grid[nr][nc], (nr, nc), (ldr, ldc), 1))

    # Turn right
    rd = complex(dr, dc) * -1j
    rdr, rdc = int(rd.real), int(rd.imag)
    nr, nc = r + rdr, c + rdc
    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
        heappush(queue, (cost + grid[nr][nc], (nr, nc), (rdr, rdc), 1))

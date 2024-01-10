import numpy as np

BOUNDS = [200000000000000, 400000000000000]
# BOUNDS = [7, 27]

stones = [[*map(int, line.strip().replace(" @", ",").split(","))] for line in open(0)]

stones = [*map(lambda x: x[:2] + x[3:-1], stones)]
lines = [*map(lambda pv: (pv[3] / pv[2], pv[1] - pv[3] / pv[2] * pv[0]), stones)]

def intersect(a: int, b: int, c: int, d: int) -> tuple[int, int]:
    if a == c:
        return None
    x = (d - b) / (a - c)
    y = a * x + b

    return x, y

def check_dir(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> bool:
    u = np.array([x1 - x2, y1 - y2])
    v = np.array([x1 - x3, y1 - y3])
    c = np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)

    return round(c) == 1

total = 0
for i, [a, b] in enumerate(lines):
    for j, [c, d] in enumerate(lines[i+1:], i+1):
        xy = intersect(a, b, c, d)
        if xy is None:
            continue
        x, y = xy

        if not (BOUNDS[0] <= x <= BOUNDS[1] and
                BOUNDS[0] <= y <= BOUNDS[1]):
            continue

        px, py, vx, vy = stones[i]
        nx, ny = px + vx, py + vy

        if not check_dir(px, py, x, y, nx, ny):
            continue

        px, py, vx, vy = stones[j]
        nx, ny = px + vx, py + vy

        if not check_dir(px, py, x, y, nx, ny):
            continue

        total += 1

print(total)

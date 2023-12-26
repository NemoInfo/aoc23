dirs = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
}

dig = [(0, 0)]
b = 0

for line in open(0):
    d, n, _ = line.split()
    dr, dc = dirs[d]
    n = int(n)

    b += n
    r, c = dig[-1]
    dig.append((r + dr * n, c + dc * n))

# Shoelace Formula
A = abs(sum(
    dig[i][0] * (dig[i - 1][1] - dig[(i + 1) % len(dig)][1])
    for i in range(len(dig)))) // 2

# Pick's Theorem
i = A - b // 2 + 1

print(i + b)

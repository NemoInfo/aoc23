patterns =[
    *map(str.splitlines, open(0).read().translate(str.maketrans(".#", "01")).split("\n\n"))
]

def check_horizontal(m):
    for r in range(len(m) - 1):
        smudge_found = False
        for i in range(min(r, len(m) - r - 2) + 1):
            diff = m[r - i] ^ m[r + 1 + i]
            if not diff:
                continue
            if not diff & (diff - 1):
                if smudge_found:
                    break
                smudge_found = True
                continue
            break
        else:
            if smudge_found:
                return r

def to_ints(m):
    return [*map(lambda x: int(x, base=2), m)]


total = 0
for pattern in patterns:
    horizontal = check_horizontal(to_ints(pattern))

    if horizontal is not None:
        total += 100 * (horizontal + 1)
        continue

    pattern_t = [
        "".join([pattern[r][c] for r in range(len(pattern))])
        for c in range(len(pattern[0]))
    ]

    total += 1 + check_horizontal(to_ints(pattern_t))

print(total)

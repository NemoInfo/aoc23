patterns = [*map(str.splitlines, open(0).read().split("\n\n"))]

def check_horizontal(pattern):
    for r in range(len(pattern) - 1):
        smudge_found = False
        for i in range(min(r, len(pattern) - r - 2) + 1):
            for c in range(len(pattern[0])):
                if pattern[r - i][c] != pattern[r + 1 + i][c]:
                    if smudge_found:
                        break
                    smudge_found = True
            else:
                continue
            break
        else:
            if smudge_found:
                return r


total = 0
for pattern in patterns:
    horizontal = check_horizontal(pattern)

    if horizontal is not None:
        total += 100 * (horizontal + 1)
        continue

    pattern_t = [
        "".join([pattern[r][c] for r in range(len(pattern))])
        for c in range(len(pattern[0]))
    ]

    total += 1 + check_horizontal(pattern_t)

print(total)

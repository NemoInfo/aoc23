from math import inf
from copy import deepcopy

block, _ = [*map(str.splitlines, open(0).read().split("\n\n"))]

ranges = {
    c: [1, 4000] for c in "xmas"
}

workflows = {}
for row in block:
    key, rules = row[:-1].split("{")
    rules = rules.split(",")
    workflows[key] = ([], rules.pop())
    for rule in rules:
        comp, next_workflow = rule.split(":")
        var = comp[0]
        op = comp[1]
        num = int(comp[2:])
        workflows[key][0].append(
            (var, op, num, next_workflow)
        )

f = {
    ">": max,
    "<": min,
}

def count(ranges, key="in"):
    if key == "A":
        prod = 1
        for s, e in ranges.values():
            prod *= e - s + 1
        return prod
    if key == "R":
        return 0
    rules, fallback = workflows[key]
    sum = 0
    for var, op, num, dst in rules:
        ci = "><".find(op)
        new_ranges = deepcopy(ranges)
        new_ranges[var][ci] = f[op](ranges[var][ci], num + [1, -1][ci])
        if new_ranges[var][0] <= new_ranges[var][1]:
            sum += count(new_ranges, key=dst)
            ranges[var][1 - ci] = f["<>"[ci]](ranges[var][1 - ci], num)
            if ranges[var][0] > ranges[var][1]:
                return sum

    return sum + count(ranges, key=fallback)

print(count(ranges))

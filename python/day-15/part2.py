strings = open(0).read().strip().split(",")
operations = [
    string.split("-") if "-" in string else string.split("=")
    for string in strings
]

def hash(s):
    sum = 0
    for c in s:
        sum += ord(c)
        sum *= 17
        sum %= 256
    return sum

d = [{} for _ in range(256)]
for label, val in operations:
    key = hash(label)
    if val:
        d[key][label] = val
    elif label in d[key]:
        del d[key][label]

total = 0
for bi, box in enumerate(d, 1):
    for hi, val in enumerate(box.values(), 1):
        total += bi * hi * int(val)

print(total)

strings = open(0).read().strip().split(",")

def hash(s):
    sum = 0
    for c in s:
        sum += ord(c)
        sum *= 17
        sum %= 256
    return sum

total = 0
for string in strings:
    total += hash(string)

print(total)

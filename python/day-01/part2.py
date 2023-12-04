import re


words = "one two three four five six seven eight nine ten".split()
regex = "(?=(" + "|".join(words) + "|\\d))"


def digit(s):
    if s.isdigit():
        return s
    return str(words.index(s) + 1)

s = 0
for line in open(0):
    digits = re.findall(regex, line)

    s += int(digit(digits[0]) + digit(digits[-1]))

print(s)

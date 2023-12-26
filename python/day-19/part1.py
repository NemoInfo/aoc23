workflows, parts = open(0).read().split("\n\n")

workflows = {
    line.split("{")[0]: [
        (lambda x, m, a, s: True, rule)
        if ":" not in rule else
        (lambda x, m, a, s, cond=(rule.split(":")[0]): eval(cond), rule.split(":")[1])
        for rule in line.split("{")[1][:-1].split(",")
    ]
    for line in workflows.splitlines()
}

def process(workflow, part):
    for rule, redirect in workflow:
        if rule(*part):
            return redirect
    raise ValueError("Wait what?")

total = 0
for part in parts.splitlines():
    part = [*map(lambda x: int(x.split("=")[1]), part[1:-1].split(","))]

    workflow = "in"
    while workflow not in "AR":
        workflow = process(workflows[workflow], part)

    if workflow == "R":
        continue

    total += sum(part)

print(total)

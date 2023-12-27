from collections import deque

class Module:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs

class FlipFlop(Module):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.mem = False

    def __repr__(self):
        return "%" + self.name + "{out=" + ",".join(self.outputs) + ", mem=" + str(self.mem) + "}"

class Conjunction(Module):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.mem = {}

    def __repr__(self):
        return "&" + self.name + "{out=" + ",".join(self.outputs) + ", mem=" + str(self.mem) + "}"

modules = {}
broadcast_dst = []

for line in open(0):
    left, right = line.strip().split(" -> ")
    outputs = right.split(", ")
    if left == "broadcaster":
        broadcast_dst = outputs
        continue
    mod_name = left[1:]
    if left[0] == "%":
        modules[mod_name] = FlipFlop(mod_name, outputs)
    elif left[0] == "&":
        modules[mod_name] = Conjunction(mod_name, outputs)
    else:
        raise ValueError(f"Oh shit oh fuck {left[0]}")

for name, module in modules.items():
    for output in module.outputs:
        if output in modules and isinstance(modules[output], Conjunction):
            modules[output].mem[name] = False

stats = {
    False: 0,
    True: 0,
}

for _ in range(1000):
    stats[False] += 1

    q = deque([("broadcaster", dst, False) for dst in broadcast_dst])
    while q:
        src, dst, signal = q.popleft()
        stats[signal] += 1

        if dst not in modules:
            continue

        module = modules[dst]

        if isinstance(module, FlipFlop):
            if signal:
                continue
            module.mem = not module.mem
            out_signal = module.mem
        elif isinstance(module, Conjunction):
            module.mem[src] = signal
            out_signal = not all(module.mem.values())

        for output in module.outputs:
            q.append((dst, output, out_signal))


print(stats[False] * stats[True])

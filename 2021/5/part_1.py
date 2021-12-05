with open("input.txt", "r") as f:
    f_lines = [l.rstrip("\n") for l in f.readlines()]

lines = []

for l in f_lines:
    line = [tuple(map(int, s.split(","))) for s in l.split(" -> ")]
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:  # no diag
        lines.append(line)

points = []

for line in lines:
    x1 = min(p[0] for p in line)
    x2 = max(p[0] for p in line)
    y1 = min(p[1] for p in line)
    y2 = max(p[1] for p in line)

    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            points.append((x, y))

d = {}

for p in points:
    if p in d:
        d[p] += 1
    else:
        d[p] = 1

print(len({k: v for k, v in d.items() if v >= 2}))

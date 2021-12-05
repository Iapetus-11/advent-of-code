from dataclasses import dataclass

with open("input.txt", "r") as f:
    flines = [l.rstrip("\n") for l in f.readlines()]

points = []

for l in flines:
    line = [tuple(map(int, s.split(","))) for s in l.split(" -> ")]
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:  # no diag
        points.extend(line)

print(points)

d = {}

for p in points:
    if p in d:
        d[p] += 1
    else:
        d[p] = 1

print(len({k: v for k, v in d.items() if v >= 2}))

for i in range(max([p[0] for p in points])+1):
    for j in range(max([p[1] for p in points])+1):
        if (c:=points.count((j, i))) != 0:
            print(c, end="")
        else:
            print(".", end="")
    print()

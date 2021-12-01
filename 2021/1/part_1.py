with open("input.txt", "r") as f:
    lines = [l for l in f.readlines() if l != "\n"]

measurements = list(map(int, lines))
last = measurements[0]

increases = 0

for m in measurements[1:]:
    if m > last:
        increases += 1

    last = m

print(increases)


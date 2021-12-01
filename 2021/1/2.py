with open("input.txt", "r") as f:
    lines = [l for l in f.readlines() if l != "\n"]

measurements = list(map(int, lines))
last = measurements[0]

increases = 0

for i in range(1, len(measurements)//3*3):
    s = sum(measurements[i:i+3])
    if s > last:
        increases += 1

    last = s


print(increases)


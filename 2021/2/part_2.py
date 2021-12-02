with open("input.txt") as f:
    lines = f.readlines()

aim = 0
h = 0
d = 0

for l in lines:
    if l != "\n":
        a,v = l.split(" ")
        v = int(v)
        if a == "forward":
            h += v
            d += aim*v
        elif a == "down":
            aim += v
        elif a == "up":
            aim -= v
        else:
            raise ValueError(l)

print(h*d)

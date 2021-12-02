with open("input.txt") as f:
    lines = f.readlines()

h = 0
d = 0

for l in lines:
    if l != "\n":
        a,v = l.split(" ")
        v = int(v)
        if a == "forward":
            h += v
        elif a == "down":
            d += v
        elif a == "up":
            d -= v
        else:
            raise ValueError(l)

print(h*d)

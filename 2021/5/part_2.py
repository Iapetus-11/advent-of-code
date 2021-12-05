with open("input.txt", "r") as f:
    f_lines = [l.rstrip("\n") for l in f.readlines()]

lines = []

class Line:
    def __init__(self, coords, straight):
        self.coords = coords
        self.straight = straight

    def genpoints(self) -> list[tuple[int, int]]:
        if self.straight:
            x1 = min(p[0] for p in self.coords)
            x2 = max(p[0] for p in self.coords)
            y1 = min(p[1] for p in self.coords)
            y2 = max(p[1] for p in self.coords)

            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    yield (x, y)
        else:
            ps_s_min2max = sorted(self.coords)
            x1, y1 = ps_s_min2max[0]
            x2, y2 = ps_s_min2max[1]
            
            rise = y2 - y1
            run = x2 - x1

            slope = rise // run

            x = x1
            y = y1

            while (x, y) != (x2, y2):
                yield (x, y)
                x += 1
                y += slope

            yield (x2, y2)

for l in f_lines:
    line = [tuple(map(int, s.split(","))) for s in l.split(" -> ")]
    lines.append(Line(line, (line[0][0] == line[1][0] or line[0][1] == line[1][1])))

points = []

for line in lines:
    points.extend(line.genpoints())

d = {}

for p in points:
    if p in d:
        d[p] += 1
    else:
        d[p] = 1

print(len({k: v for k, v in d.items() if v >= 2}))

import std/[strutils, sugar]

let
    data = readFile("input.txt")
    lines = data.strip(true, true, {'\n', '\r', ' '}).splitLines()

    positions = collect(newSeq):
        for l in lines[0].split({','}):
            l.parseInt

    pMin = positions.min
    pMax = positions.max

var fuelUsages = newSeq[int]()

for i in pMin .. pMax:
    var fuel = 0

    for p in positions:
        let steps = abs(i - p)
        fuel += ((steps * (steps + 1)) / 2).toInt

    fuelUsages.add(fuel)

echo min(fuelUsages)

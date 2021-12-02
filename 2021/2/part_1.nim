import std/[strutils]

let
    data = readFile("input.txt")
    lines = data.splitLines

var h, d: int

for l in lines:
    if l == "\n":
        continue

    let split = l.split(" ")

    if split.len != 2:
        continue

    let
        a = split[0]
        v = split[1].parseInt

    case a:
    of "forward": h += v
    of "down": d += v
    of "up": d -= v
    else: discard

echo h * d

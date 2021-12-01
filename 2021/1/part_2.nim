# nim doesn't like file that start with numbers, reasonable ig

import std/[strutils, sequtils]

let
    input = readFile("input.txt")
    lines: seq[string] = input.splitLines().toSeq

var
    increases = 0
    last = -1
    measurements = newSeq[int]()

for line in lines:
    try:
        measurements.add(line.parseInt)
    except ValueError:
        discard

last = measurements[0]

proc sum(s: seq[int]): int =
    for i in s:
        result += i

for i in 1 .. measurements.high:
    let s = measurements[i .. min(i+2, measurements.high)].sum

    if s > last:
        increases += 1

    last = s

echo increases

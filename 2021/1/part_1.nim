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

for m in measurements[1 .. measurements.high]:
    if m > last:
        increases += 1

    last = m

echo increases

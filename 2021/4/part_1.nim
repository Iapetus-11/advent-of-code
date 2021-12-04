import std/[tables, strutils, sugar]

type
    Board = ref object
        m*: var seq[seq[bool]]
        a*: var seq[seq[int]]

var
    fd = readFile("input.txt")
    lines = collect(newSeq):
        for line in fd.splitLines():
            line.strip(true, true, {'\n', ' '})
    balls = lines[0].split(",")
    boards = newSeq[Board]()

lines = lines[1..lines.high]

for l in lines:
    if l == "":
        boards.add(Board())
    else:
        boards[boards.high].b.add(l.split(" "))

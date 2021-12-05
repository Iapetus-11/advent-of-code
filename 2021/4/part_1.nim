import std/[tables, strutils, sugar]

type
    Board = ref object
        m*: seq[seq[bool]]
        a*: seq[seq[string]]

var
    fd = readFile("input.txt")
    lines = collect(newSeq):
        for line in fd.splitLines():
            line.strip(true, true, {'\n', ' '})
    balls = lines[0].split(",")
    boards = newSeq[Board]()

lines = lines[1..lines.high]

proc initSMat[T](v: T, s: int): seq[seq[T]] =
    for i in 0 .. s-1:
        var r = newSeq[T]()
        for j in 0 .. s-1:
            r.add(v)
        result.add(r)

proc initBoard(): Board =
    return Board(m: initSMat(false, 5), a: @[])

for l in lines:
    if l == "":
        boards.add(initBoard())
    else:
        boards[boards.high].a.add(l.split(" "))

proc all[T](s: seq[T]): bool =
    for e in s:
        if not bool(e):
            return false

    return true

proc isBingo(b: Board): bool =
    for i in 0..4:
        if all(b.m[i]) or all(@[b.m[0][i], b.m[1][i], b.m[2][i], b.m[3][i], b.m[4][i]]):
            return true

    return false

proc getUnmarked(b: Board): seq[string] =
    for i in 0..4:
        for j in 0..4:
            if not b.m[i][j]:
                result.add(b.a[i][j])

proc sumMapInt(s: seq[string]): int =
    for e in s:
        try:
            result += e.parseInt
        except ValueError:
            discard

for c in balls:
    for b in boards:
        for i in 0..4:
            for j in 0..4:
                if b.a[i][j] == c:
                    b.m[i][j] = true

                if isBingo(b):
                    echo sumMapInt(getUnmarked(b)), " ", c
                    echo sumMapInt(getUnmarked(b)) * c.parseInt
                    quit 0

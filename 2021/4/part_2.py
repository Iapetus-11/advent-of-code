with open("input.txt", "r") as f:
    lines = [l.rstrip("\n") for l in f.readlines()]

with open("input.txt", "r") as f:
    lines = [l.rstrip("\n") for l in f.readlines()]

choices = lines[0].split(",")
lines = lines[1:]
boards = []

for l in lines:
    if l == "":
        boards.append({"m": [[False]*5 for _ in range(5)], "b": []})
    else:
        boards[-1]["b"].append(l.split())


def is_bingo(b: dict) -> bool:
    for i in range(5):
        if all(b["m"][i]) or all([b["m"][0][i], b["m"][1][i], b["m"][2][i], b["m"][3][i], b["m"][4][i]]):
            return True

    return False

def get_unmarked(b: dict):
    for i in range(5):
        for j in range(5):
            if not b["m"][i][j]:
                yield b["b"][i][j]

won = {}

for c in choices:
    for idxb, b in enumerate(boards):
        if idxb not in won:
            for i in range(5):
                for j in range(5):
                    if b["b"][i][j] == c:
                        b["m"][i][j] = True

                    if is_bingo(b):
                        # print(sum(map(int, get_unmarked(b))), c)
                        # print(sum(map(int, get_unmarked(b)))* int(c))
                        # exit()
                        won[idxb]= sum(map(int, get_unmarked(b))) * int(c)

print(list(won.values())[-1])

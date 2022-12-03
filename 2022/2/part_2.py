with open("input.txt", "r") as f:
    lines = f.read().split('\n')

enemy_plays = 'ABC'
your_plays = 'XYZ'


def _get_score(enemy: str, you: str) -> int:
    if you == "X":
        you = your_plays[enemy_plays.index(enemy) - 1]
    elif you == "Y":
        you = your_plays[enemy_plays.index(enemy)]
    else:
        you = your_plays[(enemy_plays.index(enemy) + 1) % 3]

    score = your_plays.index(you) + 1

    if enemy == enemy_plays[your_plays.index(you)]:
        score += 3
    else:
        score += (your_plays[(enemy_plays.index(enemy) + 1) % 3] == you) * 6

    return score

score = 0
for enemy, _, you in lines:
    score += _get_score(enemy, you)
print(score)
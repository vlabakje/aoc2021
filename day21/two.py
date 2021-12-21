from functools import cache

def hundred_sided_die():
    for i in range(1, 2**40):
        yield i

def turn(pos, dice):
    pos += next(dice) + next(dice) + next(dice)
    if pos % 10 == 0:
        return 10
    return pos % 10


@cache
def wins(p1_pos, p1_score, p2_pos, p2_score):
    if p1_score >= 21:
        return (1, 0)
    if p2_score >= 21:
        return (0, 1)
    total_p1, total_p2 = 0, 0
    # roll p1
    for die1 in range(1, 4):
        for die2 in range(1, 4):
            for die3 in range(1, 4):
                new_pos = (p1_pos + die1 + die2 + die3) % 10
                new_score = p1_score + new_pos + 1

                p2_wins, p1_wins = wins(p2_pos, p2_score, new_pos, new_score)
                total_p1 += p1_wins
                total_p2 += p2_wins
    return total_p1, total_p2

def game():
    p1, p2 = wins(8-1, 0, 7-1, 0)
    print(max(p1, p2))

if __name__ == "__main__":
    game()

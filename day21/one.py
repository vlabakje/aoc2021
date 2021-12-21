
def hundred_sided_die():
    for i in range(1, 2**40):
        yield i

def turn(pos, dice):
    pos += next(dice) + next(dice) + next(dice)
    if pos % 10 == 0:
        return 10
    return pos % 10


def game():
    p1 = 8
    p2 = 7
    p1_score = 0
    p2_score = 0
    dice = hundred_sided_die()
    times_rolled = 0
    while p1_score < 1000 and p2_score < 1000:
        p1 = turn(p1, dice)
        p1_score += p1
        times_rolled += 3
        if p1_score >= 1000:
            break
        p2 = turn(p2, dice)
        p2_score += p2
        times_rolled += 3
        print(f"{p1=} {p1_score=} {p2=} {p2_score=}")
    print(f"{p1_score=} {p2_score=}")
    if p1_score > p2_score:
        print(times_rolled * p2_score)
    else:
        print(times_rolled * p1_score)

if __name__ == "__main__":
    game()

def shoot(vx, vy, target):
    x, y, step, top_y = 0, 0, 0, 0
    while y > target[2] and x <= target[1]:
        x += max(0, vx-step)
        y += vy-step
        step += 1
        top_y = max(top_y, y)
        if (target[0] <= x <= target[1]) and (target[2] <= y <= target[3]):
            #print(f"{vx},{vy} hit {x=} {y=} {target=} {vx=} {vy=} {top_y=}")
            return top_y


def parse_target(target):
    x, _, y = target[len("target area: "):].partition(", ")
    return list(map(int, x[2:].split(".."))) + list(map(int, y[2:].split("..")))


def min_vx(target_x):
    for i in range(target_x):
        result = sum(max(0, i-j) for j in range(target_x))
        if result > target_x:
            return i


def distinct_velocities(target):
    v = set()
    for vx in range(min_vx(target[0]), target[1]+1):
        for vy in range(min(target[2], target[3]), max(abs(target[2]), abs(target[3]))):
            if shoot(vx, vy, target) != None:
                v.add((vx, vy))
    return len(v)


if __name__ == "__main__":
    assert distinct_velocities(parse_target("target area: x=20..30, y=-10..-5")) == 112
    print(distinct_velocities(parse_target("target area: x=119..176, y=-141..-84")))

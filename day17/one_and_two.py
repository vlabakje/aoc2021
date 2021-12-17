def shoot(vx, vy, target):
    x, y, step, top_y = 0, 0, 0, 0
    while y > target[2]:
        x += max(0, vx-step)
        y += vy-step
        if x > target[1]:
            return None
        top_y = max(top_y, y)
        if (target[0] <= x <= target[1]) and (target[2] <= y <= target[3]):
            #print(f"{vx},{vy} hit {x=} {y=} {target=} {vx=} {vy=} {top_y=}")
            return top_y
        step += 1
    return None


def parse_target(target):
    assert target.startswith("target area: ")
    target = target[len("target area: "):]
    x, _, y = target.partition(", ")
    target = []
    target.extend(map(int, x[2:].split("..")))
    target.extend(map(int, y[2:].split("..")))
    #print(target)
    return target


def min_vx(target_x):
    for i in range(target_x):
        result = sum(max(0, i-j) for j in range(target_x))
        if result > target_x:
            return i

def max_y(target):
    peak = None
    for vx in range(min_vx(target[0]), target[1]+1):
        for vy in range(target[2], abs(target[2])):
            if p := shoot(vx, vy, target):
                if peak is None or p > peak[2]:
                    peak = (vx, vy, p)
                    #print(f"new peak {peak=} {vy=}")
    return peak[2]


def distinct_velocities(target):
    v = set()
    for vx in range(min_vx(target[0]), target[1]+1):
        for vy in range(min(target[2], target[3]), max(abs(target[2]), abs(target[3]))):
            if shoot(vx, vy, target) != None:
                v.add((vx, vy))
    return len(v)


if __name__ == "__main__":
    assert max_y(parse_target("target area: x=20..30, y=-10..-5")) == 45
    assert distinct_velocities(parse_target("target area: x=20..30, y=-10..-5")) == 112
    print("part 1", max_y(parse_target("target area: x=119..176, y=-141..-84")))
    print("part 2", distinct_velocities(parse_target("target area: x=119..176, y=-141..-84")))

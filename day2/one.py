def instructions():
    with open("input") as finput:
        for line in finput:
            direction, _, distance = line.partition(" ")
            yield direction, int(distance)

def main():
    horizontal, depth = 0, 0
    for direction, distance in instructions():
        if direction == "down":
            depth += distance
        elif direction == "up":
            depth -= distance
        elif direction == "forward":
            horizontal += distance
        else:
            raise NotImplementedError(f"unkown direction {direction=}")
    return horizontal * depth

if __name__ == "__main__":
    print(main())

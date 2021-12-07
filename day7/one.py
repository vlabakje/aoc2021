def positions():
    with open("input") as fileh:
        return list(map(int, fileh.read().strip().split(",")))

def main():
    crabs = positions()
    move_to, distance = None, 2 ** 32
    for destination in range(max(crabs)+1):
        x = sum(abs(crab-destination) for crab in crabs)
        if distance > x:
            move_to, distance = destination, x
        #print(f"move to {destination} {x} {distance=} {move_to=}")
    return distance

if __name__ == "__main__":
    print(main())

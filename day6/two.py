def main():
    # dict mapping fish age to number of fish
    state = read_lanternfish()
    for _ in range(256):
        new_fish = state[0]
        # every fish age decreases by one, so the dict shifts left
        state = dict((i, state[i+1]) for i in range(8))
        state[6] += new_fish
        state[8] = new_fish
    return sum(state.values())

def read_lanternfish():
    with open("input") as fileh:
        fish = list(map(int, fileh.read().strip().split(",")))
        return dict((i, fish.count(i)) for i in range(9))

if __name__ == "__main__":
    print(main())

def main():
    state = read_lanternfish()
    for day in range(80):
        #print(f"After {day=} : {state=}")
        new = 0
        for i in range(8):
            state[i], old = state[i+1], state[i]
            if i == 0:
                new = old
        state[6] += new
        state[8] = new
    return sum(state.values())

def read_lanternfish():
    with open("input") as fileh:
        fish = list(map(int, fileh.read().strip().split(",")))
        return dict((i, fish.count(i)) for i in range(9))

if __name__ == "__main__":
    print(main())

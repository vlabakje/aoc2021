EXPECTED={ ")": "(", "]": "[", "}": "{", ">": "<"}
SCORE={")": 3, "]": 57, "}": 1197, ">": 25137}

def main(filename):
    total = 0
    with open(filename) as fileh:
        for line in fileh:
            total += score(line.strip())
    return total

def score(line):
    stack = []
    output = 0
    for char in line:
        if char in EXPECTED.values():
            stack.append(char)
        else:
            top = stack.pop()
            if EXPECTED[char] != top:
                return SCORE[char]
    return 0

if __name__ == "__main__":
    assert main("example") == 26397
    print(main("input"))

EXPECTED={ ")": "(", "]": "[", "}": "{", ">": "<"}
SCORE={"(": 1, "[": 2, "{": 3, "<": 4}

def main(filename):
    scores = []
    with open(filename) as fileh:
        for line in fileh:
            stack = incomplete_stack(line.strip())
            if stack:
                scores.append(score(stack))
    return sorted(scores)[int(len(scores)/2)]

def incomplete_stack(line):
    stack = []
    for char in line:
        if char in EXPECTED.values():
            stack.append(char)
        else:
            top = stack.pop()
            if EXPECTED[char] != top:
                return []
    return stack

def score(stack):
    total = 0
    for item in stack[::-1]:
        total *= 5
        total += SCORE[item]
    return total

if __name__ == "__main__":
    assert main("example") == 288957
    print(main("input"))

with open("input") as fileh:
    count = 0
    for line in fileh:
        samples, _, output = line.strip().partition(" | ")
        for digit in output.split(" "):
            if len(digit) in (2, 3, 4, 7):
                count += 1
    print(count)

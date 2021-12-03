def main():
    report = list(report_lines())
    number_of_bits = len(report[0])
    gamma, epsilon = 0, 0
    for i, count in enumerate(bitcount(report)):
        if count > len(report)/2:
            gamma |= (1 << (number_of_bits - i - 1))
        else:
            epsilon |= (1 << (number_of_bits - i - 1))
    #print(f"{number_of_bits=} {gamma=} {epsilon=} {bin(gamma)}")
    return gamma * epsilon

def bitcount(report):
    output = [0 for _ in report[0]]
    for value in report:
        for i, b in enumerate(value):
            if b == "1":
                output[i] += 1
    return output

def report_lines():
    with open("input") as fileh:
        for line in fileh:
            yield line.strip()

if __name__ == "__main__":
    print(main())

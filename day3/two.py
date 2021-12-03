def main():
    report = list(report_lines())
    oxygen = rating(report[:], co2=False)
    co2 = rating(report[:], co2=True)
    return oxygen * co2

def rating(report, co2):
    for bit in range(len(report[0])):
        looking_for = "1" if (bitcount(report, bit) >= len(report)/2) != co2 else "0"
        report = [v for v in report if v[bit] == looking_for]
        if len(report) == 1:
            return int(report[0], 2)

def bitcount(report, bit):
    return sum(1 for value in report if value[bit] == "1")

def report_lines():
    with open("input") as fileh:
        for line in fileh:
            yield line.strip()

if __name__ == "__main__":
    print(main())

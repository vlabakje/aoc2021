def readings():
    with open("input") as finput:
        for line in finput:
            yield int(line)


def increases():
    prev = None
    for reading in readings():
        if prev:
            if reading > prev:
                yield 1
        prev = reading

def main():
    print(sum(increases()))

if __name__ == "__main__":
    main()

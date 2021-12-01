from collections import deque

def readings():
    with open("input") as finput:
        for line in finput:
            yield int(line)

def sliding_window(iterable, size):
    window = deque(maxlen=size)
    for _ in range(size):
        window.append(next(iterable))
    yield sum(window)
    for i in iterable:
        window.popleft()
        window.append(i)
        yield sum(window)

def increases():
    prev = None
    for reading in sliding_window(readings(), 3):
        if prev:
            if reading > prev:
                yield 1
        prev = reading

def main():
    print(sum(increases()))

if __name__ == "__main__":
    main()

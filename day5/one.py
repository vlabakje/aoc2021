from dataclasses import dataclass

@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

def main():
    max_x, max_y, lines = read_lines()
    # init grid
    grid = [[0] * (max_x+1) for _ in range(max_y+1)]
    for line in lines:
        for x, y in points_on_line(line):
            grid[y][x] += 1
    print_grid(grid)
    counter = 0
    for row in grid:
        for cell in row:
            if cell > 1:
                counter += 1
    return counter


def print_grid(grid):
    for row in grid:
        print("".join(str(i) for i in row))

def points_on_line(line):
    if line.x1 == line.x2:
        for y in range(min(line.y1, line.y2), max(line.y1, line.y2)+1):
            yield line.x1, y
    elif line.y1 == line.y2:
        for x in range(min(line.x1, line.x2), max(line.x1, line.x2)+1):
            yield x, line.y1
    else:
        raise NotImplementedError("faal")

def read_lines():
    max_x, max_y = 0, 0
    lines = []
    with open("input") as fileh:
        for line in fileh:
            one, _, two = line.partition(" -> ")
            x1, y1 = map(int, one.split(","))
            x2, y2 = map(int, two.split(","))
            if not (x1 == x2 or y1 == y2):
                print(f"warning ignore reading {line.strip()}")
                continue
            max_x = max(max_x, x1, x2)
            max_y = max(max_y, y1, y2)
            lines.append(Line(x1, y1, x2, y2))
    return max_x, max_y, lines

if __name__ == "__main__":
    print(main())

class Grid():
    def __init__(self, filename):
        self.grid = []
        with open(filename) as fileh:
            for line in fileh:
                self.grid.append(list(map(int, line.strip())))
        assert len(self.grid)
        self.x = len(self.grid[0])
        self.y = len(self.grid)
        assert sum(len(line) for line in self.grid) == self.x * self.y

    def neighbours(self, x, y):
        for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < len(self.grid[0]):
                if 0 <= ny < len(self.grid):
                    yield self.grid[ny][nx]

    def low_point_risks(self):
        for x in range(self.x):
            for y in range(self.y):
                if self.grid[y][x] < min(self.neighbours(x, y)):
                    # print(f"{x=} {y=} {self.grid[y][x]=} {min(self.neighbours(x, y))=}")
                    yield self.grid[y][x] + 1


def main():
    grid = Grid("input")
    print(sum(grid.low_point_risks()))


if __name__ == "__main__":
    main()

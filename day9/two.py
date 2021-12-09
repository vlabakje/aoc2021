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
        for nx, ny in self.neighbour_coords(x, y):
            yield self[nx][ny]

    def neighbour_coords(self, x, y):
        for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < len(self.grid[0]):
                if 0 <= ny < len(self.grid):
                    yield nx, ny

    def low_points(self):
        for x in range(self.x):
            for y in range(self.y):
                if self[x][y] < min(self.neighbours(x, y)):
                    # print(f"{x=} {y=} {self.grid[y][x]=} {min(self.neighbours(x, y))=}")
                    yield x, y

    def basin_coords(self, x, y):
        # given low point, yield all basin coordinates
        yield x, y  # this point is part of the basin too!
        seen = set()
        todo = set([(x,y)])
        while len(todo):
            todo_next = set()
            for x, y in set(todo):
                seen.add((x, y))
                for nx, ny in self.neighbour_coords(x, y):
                    if (nx, ny) not in seen:
                        if self[nx][ny] != 9:
                            yield nx, ny
                            seen.add((nx, ny))
                            todo_next.add((nx, ny))
            todo = todo_next

    def basin_size(self, x, y):
        return len(list(self.basin_coords(x, y)))

    def __getitem__(self, item):
        return [line[item] for line in self.grid]


def main():
    grid = Grid("input")
    basin_sizes = []
    for x, y in grid.low_points():
        basin_sizes.append(grid.basin_size(x, y))
    total = 1
    for _ in range(3):
        m = max(basin_sizes)
        total *= m
        basin_sizes.remove(m)
    print(total)


if __name__ == "__main__":
    main()

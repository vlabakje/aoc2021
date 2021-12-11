class Grid:
    def __init__(self, filename):
        self._grid = []
        with open(filename) as fileh:
            for line in fileh:
                self._grid.append(list(map(int, line.strip())))
                assert len(self._grid[-1])
            assert len(self._grid)
        self.x = len(self._grid[0])
        self.y = len(self._grid)

    def __getitem__(self, item):
        return self._grid[item[1]][item[0]]
    
    def __setitem__(self, item, value):
        self._grid[item[1]][item[0]] = value

    def __str__(self):
        output = ""
        for line in self._grid:
            output += "".join(map(str, line)) + "\n"
        return output
    
    def increment(self):
        for x in range(self.x):
            for y in range(self.y):
                self[x, y] += 1
                if self[x, y] == 10:
                    self.flash(x, y)
        flashes = 0
        for x in range(self.x):
            for y in range(self.y):
                if self[x, y] > 9:
                    self[x, y] = 0
                    flashes += 1
        return flashes

    def flash(self, x, y):
        for nx, ny in self.neighbours(x, y):
            self[nx, ny] += 1
            if self[nx, ny] == 10:
                self.flash(nx, ny)
    
    def neighbours(self, x, y):
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if (dx, dy) != (0, 0) and 0 <= x+dx < self.x and 0 <= y+dy < self.y:
                    yield x+dx, y+dy

def flashes(filename):
    total = 0
    grid = Grid(filename)
    print(f"start\n{grid}")
    for step in range(100):
        total += grid.increment()
        print(f"{step=} {total=}\n{grid}")
    return total

if __name__ == "__main__":
    assert flashes("smallexample") == 259
    assert flashes("example") == 1656
    print(flashes("input"))

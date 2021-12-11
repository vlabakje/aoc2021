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

def flash(filename):
    grid = Grid(filename)
    for step in range(1000):
        count = grid.increment()
        if count == grid.x * grid.y:
            return step+1

if __name__ == "__main__":
    assert flash("example") == 195
    print(flash("input"))

class Grid():
    def __init__(self, lines, algo_line):
        self.algo = dict((i, c == "#") for i, c in enumerate(algo_line.strip()))
        self.lit = set()
        self.min_x = self.min_y = self.max_x = self.max_y = 0
        for y, line in enumerate(lines.strip().split("\n")):
            for x, c in enumerate(line.strip()):
                self[x, y] = (c == "#")
        for x, y in self.lit:
            self.max_x = max(self.max_x, x)
            self.max_y = max(self.max_y, y)
        self.outside_grid = False

    def __getitem__(self, xy):
        if (self.min_x <= xy[0] <= self.max_x) and (self.min_y <= xy[1] <= self.max_y):
            return (xy[0], xy[1]) in self.lit
        return self.outside_grid

    def __setitem__(self, xy, value):
        if value:
            self.lit.add((xy[0], xy[1]))
        else:
            self.lit.discard((xy[0], xy[1]))

    def apply_algo(self):
        new_lit = set()
        for x in range(self.min_x-2, self.max_x+3):
            for y in range(self.min_y-2, self.max_y+3):
                if self.algo[self.surrounding(x, y)]:
                    new_lit.add((x, y))
        self.lit = new_lit
        self.min_x -= 2
        self.max_x += 2
        self.min_y -= 2
        self.max_y += 2
        self.outside_grid = self.algo[511 if self.outside_grid else 0]

    def surrounding(self, x, y):
        state = 0
        bit = 8
        for dy in (-1, 0 , 1):
            for dx in (-1, 0, 1):
                state |= self[x+dx,y+dy] << bit
                #print(f"{x+dx=} {y+dy=} {self[x+dx,y+dy]=} {bin(state)=}")
                bit -= 1
        return state
                
    def __str__(self):
        output = ""
        for y in range(self.min_y-2, self.max_y+3):
            output += "".join("#" if self[x, y] else "." for x in range(self.min_x-2, self.max_x+3)) + "\n"
        return output

def lit_pixels(filename):
    al, gl = open(filename).read().split("\n\n")
    grid = Grid(gl, al)
    for i in range(2):
        grid.apply_algo()
        print(len(grid.lit))


if __name__ == "__main__":
    lit_pixels("input")

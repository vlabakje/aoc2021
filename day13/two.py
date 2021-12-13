class Grid():
    def __init__(self, filename):
        coords, _, folds = open(filename).read().partition("\n\n")
        self._dots = set()
        self.x = 0
        self.y = 0
        for coord in coords.split("\n"):
            x, _, y = coord.partition(",")
            self.x = max(self.x, int(x))
            self.y = max(self.y, int(y))
            self._dots.add((int(x), int(y)))
        self._folds = []
        for fold in folds.split("\n"):
            if len(fold):
                assert fold.startswith("fold along ")
                axis, _, count = fold[11:].partition("=")
                self._folds.append((axis, int(count)))

    def __str__(self):
        output = ""
        for y in range(self.y+1):
            for x in range(self.x+1):
                if (x, y) in self._dots:
                    output += "#"
                else:
                    output += "."
            output += "\n"
        return output

    def fold(self):
        for axis, count in self._folds:
            newdots = set()
            if axis == "y":
                for dot in self._dots:
                    if dot[1] > count:
                        newdots.add((dot[0], count - (dot[1] - count)))
                    else:
                        newdots.add(dot)
                self.y = count - 1
            elif axis == "x":
                for dot in self._dots:
                    if dot[0] > count:
                        newdots.add((count - (dot[0] - count), dot[1]))
                    else:
                        newdots.add(dot)
                self.x = count - 1
            self._dots = newdots


def main(filename):
    grid = Grid(filename)
    grid.fold()
    print(grid)

if __name__ == "__main__":
    main("example")
    main("input")

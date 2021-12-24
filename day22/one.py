from collections import defaultdict
class Space():
    _active = set()
    def region(self, on, range_x, range_y, range_z):
        action = self._active.discard
        if on:
            action = self._active.add
        for x in range(range_x[0], range_x[1]+1):
            for y in range(range_y[0], range_y[1]+1):
                for z in range(range_z[0], range_z[1]+1):
                    action((x, y, z))

def count_on(filename):
    s = Space()
    for line in open(filename):
        onoff, coords = line.strip().split(" ")
        onoff = onoff == "on"
        xyz = {}
        for c in coords.split(","):
            xyz[c[0]] = list(map(int, c[2:].split("..")))
        print(f"{onoff=} {xyz=}")
        if 50 < xyz["x"][0] or xyz["x"][0] < -50:
            return
        s.region(onoff, xyz["x"], xyz["y"], xyz["z"])
        print(len(s._active))

if __name__ == "__main__":
    count_on("input")

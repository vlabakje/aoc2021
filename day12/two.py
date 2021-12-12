from dataclasses import dataclass
from typing import List

@dataclass
class Node():
    name: str
    connections: List["Node"]

    @property
    def big(self):
        return self.name.isupper()

class Graph():
    def __init__(self, filename):
        self.raw_connections = [x.strip() for x in open(filename).readlines()]
        self.nodes = {}
        for rc in self.raw_connections:
            source, _, dest = rc.partition("-")
            if source not in self.nodes:
                self.nodes[source] = Node(name=source, connections=[])
            if dest not in self.nodes:
                self.nodes[dest] = Node(name=dest, connections=[])
            self.nodes[source].connections.append(self.nodes[dest])
            self.nodes[dest].connections.append(self.nodes[source])
    
    def _path(self, source, path, can_do_twice):
        for c in source.connections:
            if c.name == "end":
                yield path + [c.name]
            elif c.big:
                yield from self._path(c, path + [c.name], can_do_twice)
            else:
                if c.name in can_do_twice:
                    yield from self._path(c, path + [c.name], [])
                if c.name not in path:
                    yield from self._path(c, path + [c.name], can_do_twice)
    
    def paths(self):
        for node in self.nodes.values():
            if not node.big and not node.name in ("start", "end"):
                yield from self._path(self.nodes["start"], ["start"], [node.name])


def paths(filename):
    graph = Graph(filename)
    return len(set(list(",".join(p) for p in graph.paths())))


if __name__ == "__main__":
    assert paths("example-10") == 36
    assert paths("example-19") == 103
    assert paths("example-226") == 3509
    print(paths("input"))

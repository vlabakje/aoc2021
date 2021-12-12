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
    
    def _path(self, source, path):
        # return all possible paths from this node 
        for c in source.connections:
            if c.big or c.name not in path:
                if c.name == "end":
                    yield path + [c.name]
                else:
                    yield from self._path(c, path + [c.name])
    
    def paths(self):
        yield from self._path(self.nodes["start"], ["start"])


def paths(filename):
    graph = Graph(filename)
    #for p in graph.paths():
    #    print(",".join(p))
    return len(list(graph.paths()))


if __name__ == "__main__":
    assert paths("example-10") == 10
    assert paths("example-19") == 19
    assert paths("example-226") == 226
    print(paths("input"))

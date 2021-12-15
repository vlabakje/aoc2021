class Graph():
    def __init__(self, filename):
        self.nodes = []
        for line in open(filename):
            self.nodes.append(list(map(int, line.strip())))
            assert len(self.nodes[-1])
        self.x, self.y = len(self.nodes[0]), len(self.nodes)
        assert all(len(row) == self.x for row in self.nodes)


    def __str__(self):
        output = ""
        for row in self.nodes:
            output += "".join(map(str, row)) + "\n"
        return output
    
    def dijkstra(self):
        unvisited_nodes = set((x, y) for x in range(self.x) for y in range(self.y))
        shortest_path = [[2**64] * (self.x+1) for _ in range(self.y+1)]
        shortest_path[0][0] = 0
        previous_nodes = {}
        while unvisited_nodes:
            lowest = (self.x, self.y)
            for node in unvisited_nodes:
                if shortest_path[node[1]][node[0]] < shortest_path[lowest[1]][lowest[0]]:
                    lowest = node
            #print(f"{len(unvisited_nodes)=} {lowest=}")
            #print(pretty(shortest_path))
            for nx, ny in self.neighbours(lowest):
                path_len = shortest_path[lowest[1]][lowest[0]] + self.nodes[ny][nx]
                if path_len < shortest_path[ny][nx]:
                    shortest_path[ny][nx] = path_len
                    previous_nodes[(nx, ny)] = lowest
            unvisited_nodes.remove(lowest)
        return shortest_path[self.y-1][self.x-1]

    def neighbours(self, node):
        for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            nx, ny = node[0]+dx, node[1]+dy
            if 0 <= nx < len(self.nodes[0]):
                if 0 <= ny < len(self.nodes):
                    yield nx, ny


def pretty(graph):
    output = ""
    for row in graph:
        output += " ".join(map(str, (x for x in row if x != 2**64))) + "\n"
    return output

def pathrisk(filename):
    graph = Graph(filename)
    return graph.dijkstra()

if __name__ == "__main__":
    assert pathrisk("example") == 40
    print(pathrisk("input"))

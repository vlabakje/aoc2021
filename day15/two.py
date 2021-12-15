import heapq

class Graph():
    def __init__(self, filename):
        self.nodes = []
        for line in open(filename):
            self.nodes.append(list(map(int, line.strip())))
            assert len(self.nodes[-1])
        self.x, self.y = len(self.nodes[0]), len(self.nodes)
        assert all(len(row) == self.x for row in self.nodes)

    def duplicate(self):
        newnodes = []
        for row in self.nodes:
            newrow = row[:]
            for i in range(1, 5):
                newrow.extend(j+i if i+j < 10 else i+j-9 for j in row)
            newnodes.append(newrow)
        self.nodes, newnodes = newnodes, []
        # duplicate rows five times
        for i in range(5):
            for row in self.nodes:
                newnodes.append(list(i+j if i+j < 10 else i+j-9 for j in row))
        self.nodes = newnodes
        self.x, self.y = len(self.nodes[0]), len(self.nodes)

    def __str__(self):
        output = ""
        for row in self.nodes:
            output += "".join(map(str, row)) + "\n"
        return output
    
    def dijkstra_heapq(self, destination):
        queue = [(0, (0, 0))]
        risks = {(0, 0): 0}
        visited = {(0, 0)}
        while queue:
            risk, (x, y) = heapq.heappop(queue)
            if (x, y) == destination:
                return risk
            for nx, ny in self.neighbours((x, y)):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    path_len = risk + self.nodes[ny][nx]
                    if path_len < risks.get((nx, ny), 2**64):
                        risks[(nx, ny)] = path_len
                        heapq.heappush(queue, (path_len, (nx, ny)))

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
    graph.duplicate()
    #print(graph)
    return graph.dijkstra_heapq((graph.x-1, graph.y-1))

if __name__ == "__main__":
    assert pathrisk("example") == 315
    print(pathrisk("input"))

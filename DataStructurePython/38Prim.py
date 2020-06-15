import heapq


def Prim(graph: dict, vertex: str) -> list:
    visited = set()
    visited.add(vertex)
    path = [(vertex, 0)]
    while visited != graph.keys():
        ls = []
        for node in visited:
            for w in graph[node].keys():
                if w not in visited:
                    heapq.heappush(ls, (graph[node][w], w))
        dt, v = heapq.heappop(ls)
        visited.add(v)
        path.append((v, dt))
    return path


if __name__ == "__main__":
    g = {"A": {"B": 5, "C": 1},
         "B": {"A": 5, "C": 2, "D": 1},
         "C": {"A": 1, "B": 2, "D": 4, "E": 8},
         "D": {"B": 1, "C": 4, "E": 3, "F": 6},
         "E": {"C": 8, "D": 3},
         "F": {"D": 6}}
    result = Prim(g, "A")
    print(result)

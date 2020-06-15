import heapq
import math


def Dijkstra(graph: dict, vertex: str) -> tuple:
    queue = []
    heapq.heappush(queue, (0, vertex))
    visited = set()
    parent = {vertex: None}
    distance = {vertex: 0}
    for node in graph.keys():
        if node != vertex:
            distance[node] = math.inf

    while queue:
        dist, node = heapq.heappop(queue)
        visited.add(node)
        nodes = graph[node].keys()
        for w in nodes:
            if w not in visited:
                if distance[node] + graph[node][w] < distance[w]:
                    heapq.heappush(queue, (distance[node] + graph[node][w], w))
                    parent[w] = node
                    distance[w] = distance[node] + graph[node][w]
    return parent, distance


if __name__ == "__main__":
    g = {"A": {"B": 5, "C": 1},
         "B": {"A": 5, "C": 2, "D": 1},
         "C": {"A": 1, "B": 2, "D": 4, "E": 8},
         "D": {"B": 1, "C": 4, "E": 3, "F": 6},
         "E": {"C": 8, "D": 3},
         "F": {"D": 6}}
    par, dt = Dijkstra(g, "A")
    print(par)
    print(dt)

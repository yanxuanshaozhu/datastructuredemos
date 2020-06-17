import heapq
import math


def dijkstra(graph: dict, vertex: int) -> tuple:
    distance = {}
    for key in graph.keys():
        distance[key] = math.inf
    distance[vertex] = 0
    queue = []
    heapq.heappush(queue, (0, vertex))
    visited = set()
    visited.add(vertex)
    parent = {vertex: None}
    while queue:
        dist, node = heapq.heappop(queue)
        visited.add(node)
        nodes = graph[node].keys()
        for w in nodes:
            if w not in visited:
                length = distance[node] + graph[node][w]
                if length < distance[w]:
                    heapq.heappush(queue, (length, w))
                    parent[w] = node
                    distance[w] = length
    return distance, parent


if __name__ == "__main__":
    g = {1: {5: 12, 2: 16, 3: 15}, 2: {1: 29, 4: 13}, 3: {1: 21, 4: 7}, 4: {2: 27, 3: 19}, 5: {1: 8, 2: 32}}
    point = 5
    dt, par = dijkstra(g, point)
    print(dt)
    print(par)

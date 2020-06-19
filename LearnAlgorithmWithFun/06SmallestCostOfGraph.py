import heapq


def prim(graph: dict) -> list:
    visited = set()
    key = list(graph.keys())[0]
    visited.add(key)
    path = [(0, key)]
    while visited != graph.keys():
        ls = []
        for node in visited:
            for w in graph[node].keys():
                if w not in visited:
                    heapq.heappush(ls, (graph[node][w], w))
        dist, v = heapq.heappop(ls)
        visited.add(v)
        path.append((dist, v))
    return path


if __name__ == "__main__":
    g = {1: {5: 12, 2: 16, 3: 15}, 2: {1: 29, 4: 13}, 3: {1: 21, 4: 7}, 4: {2: 27, 3: 19}, 5: {1: 8, 2: 32}}
    print(prim(g))

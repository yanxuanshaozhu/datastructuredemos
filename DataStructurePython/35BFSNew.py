def bfs(graph: dict, vertex: str) -> None:
    queue = []
    visited = set()
    queue.append(vertex)
    visited.add(vertex)
    while queue:
        cur = queue.pop(0)
        vertices = graph[cur]
        for v in vertices:
            if v not in visited:
                queue.append(v)
                visited.add(v)
        print(cur)


if __name__ == "__main__":
    g = {"A": {"B", "C"},
         "B": {"A", "C", "D"},
         "C": {"A", "B", "D", "E"},
         "D": {"B", "C", "E", "F"},
         "E": {"C", "D"},
         "F": {"D"}}
    bfs(g, "A")

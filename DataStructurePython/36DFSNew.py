def dfs(graph: dict, vertex: str) -> None:
    stack = []
    visited = set()
    stack.append(vertex)
    visited.add(vertex)
    while stack:
        cur = stack.pop()
        vertices = graph[cur]
        for v in vertices:
            if v not in visited:
                stack.append(v)
                visited.add(v)
        print(cur)


if __name__ == "__main__":
    g = {"A": {"B", "C"},
         "B": {"A", "C", "D"},
         "C": {"A", "B", "D", "E"},
         "D": {"B", "C", "E", "F"},
         "E": {"C", "D"},
         "F": {"D"}}
    dfs(g, "A")

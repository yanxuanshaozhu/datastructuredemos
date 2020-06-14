from collections import defaultdict


def build_graph(board_size: int) -> defaultdict:
    graph = defaultdict(set)
    for row in range(board_size):
        for col in range(board_size):
            MOVE_OFFSETS = (
                (-1, -2), (1, -2),
                (-2, -1), (2, -1),
                (-2, 1), (2, 1),
                (-1, 2), (1, 2),
            )
            for row_offset, col_offset in MOVE_OFFSETS:
                if 0 <= row + row_offset < board_size and 0 <= col + col_offset < board_size:
                    to_row, to_col = row + row_offset, col + col_offset
                    graph[(row, col)].add((to_row, to_col))
                    graph[(to_row, to_col)].add((row, col))
    return graph


def first_true(sequence):
    for item in sequence:
        if item:
            return item
    return None


def find_solution_for(board_size: int):
    graph = build_graph(board_size)
    total_squares = board_size * board_size

    def traverse(path, current_vertex):
        if len(path) + 1 == total_squares:
            # including the current square, we've visited every square,
            # so return the path as a solution
            return path + [current_vertex]

        yet_to_visit = graph[current_vertex] - set(path)
        # graph[current_vertex] :当前节点的邻接点集合
        # set(path): 走过的点的集合
        # 如果yet_to_visit是空集，就说明当前节点的所有邻接点都走过了，但是上面path+1没走完，说明此路不通GG；
        # 如果yet_to_visit不是空集，说明当前节点的邻接点里面还有没走过的，所以可以继续走
        if not yet_to_visit:
            # no unvisited neighbors, so dead end
            return False

        # try all valid paths from here
        next_vertices = sorted(yet_to_visit)
        return first_true(traverse(path + [current_vertex], vertex)
                          for vertex in next_vertices)

    # try to find a solution from any square on the board
    return first_true(traverse([], starting_vertex)
                      for starting_vertex in graph)


if __name__ == "__main__":

    print(find_solution_for(5))

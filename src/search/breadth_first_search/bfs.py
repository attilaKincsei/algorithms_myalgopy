def create_graph(nums):
    graph = dict()
    for idx, number in enumerate(nums):
        graph[idx] = list(range(min([len(nums) - 1, idx + 1]), min(len(nums), idx + 1 + number)))
    return graph


def test_fun(nums):
    graph = create_graph(nums)
    print(f"graph: {graph}")
    node_source = 0
    node_target = len(nums) - 1
    visited = set()
    to_visit = [node_source]
    paths = [[node_source]]
    while 0 < len(to_visit):
        node_current = to_visit.pop(0)
        nodes_child = graph.get(node_current)
        if nodes_child is not None:
            visited.add(node_current)
            for item in nodes_child:
                if item not in visited:
                    to_visit.append(item)
            paths_iter = paths[:]
            for path in paths_iter:
                if path[-1] == node_target:
                    continue
                if node_current == path[-1]:
                    is_delete = False
                    for node in nodes_child:
                        if node not in path:
                            is_delete = True
                            paths.append(path + [node])
                    if is_delete:
                        paths.remove(path)
    shortest_count = len(nums)
    for idx, path in enumerate(paths):
        if len(path) < shortest_count and path[-1] == node_target:
            shortest_count = len(path) - 1
    return paths


def main():
    test_input4 = [6, 2, 6, 1, 7, 9, 3, 5, 3, 7, 2, 8]
    return test_fun(test_input4)


if __name__ == '__main__':
    print(main())

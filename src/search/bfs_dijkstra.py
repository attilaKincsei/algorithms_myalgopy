
def shortest_path(graph, source, target):
    path_list = [[source]]
    path_index = 0
    # To keep track of previously visited nodes
    visited_nodes = {source}
    if source == target:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]  # get last element of current path
        next_nodes = graph[last_node]
        # Search goal node
        if target in next_nodes:
            current_path.append(target)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if next_node not in visited_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                visited_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
        print(f"path_list: {path_list}")
        print(f"visited_nodes: {visited_nodes}")
    # No path is found
    return []


if __name__ == '__main__':
    input1 = dict()
    input1[1] = {2, 5}
    input1[2] = {1, 3, 5}
    input1[3] = {2, 4}
    input1[4] = {3, 5, 6}
    input1[5] = {1, 2, 4}
    input1[6] = {4}
    print(shortest_path(input1, 1, 6))

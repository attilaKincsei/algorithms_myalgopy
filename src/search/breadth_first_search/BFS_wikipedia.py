# from collections import deque
#
#
# def breadth_first_search(problem):
#     # a FIFO open_set
#     open_set = deque()
#
#     # an empty set to maintain visited nodes
#     closed_set = set()
#
#     # a dictionary to maintain meta information (used for path formation)
#     # key -> (parent state, action to reach child)
#     meta = dict()
#
#     # initialize
#     root = problem.get_root()
#     meta[root] = (None, None)
#     open_set.append(root)
#
#     # For each node on the current level expand and process, if no children
#     # (leaf) then unwind
#     while len(open_set) != 0:
#
#         subtree_root = open_set.popleft()
#
#         # We found the node we wanted so stop and emit a path.
#         if problem.is_goal(subtree_root):
#             return construct_path(subtree_root, meta)
#
#         # For each child of the current tree process
#         for (child, action) in problem.get_successors(subtree_root):
#
#             # The node has already been processed, so skip over it
#             if child in closed_set:
#                 continue
#
#             # The child is not enqueued to be processed, so enqueue this level of
#             # children to be expanded
#             if child not in open_set:
#                 meta[child] = (subtree_root, action)  # create metadata for these nodes
#                 open_set.append(child)  # enqueue these nodes
#
#         # We finished processing the root of this subtree, so add it to the closed
#         # set
#         closed_set.add(subtree_root)
#
#
# # Produce a backtrace of the actions taken to find the goal node, using the
# # recorded meta dictionary
# def construct_path(state, meta):
#     action_list = list()
#
#     # Continue until you reach root metadata (i.e. (None, None))
#     while meta[state][0] is not None:
#         state, action = meta[state]
#         action_list.append(action)
#
#     action_list.reverse()
#     return action_list

def shortest_path(graph, node_source, node_target):
    paths = [[node_source]]
    path_idx = 0
    # To keep track of previously visited nodes
    visited = {node_source}
    if node_source == node_target:
        return paths[0]

    while path_idx < len(paths):
        path_current = paths[path_idx]
        node_current = path_current[-1]
        nodes_child = graph[node_current]
        # Search goal node
        if node_target in nodes_child:
            path_current.append(node_target)
            return path_current
        # Add new paths
        for node in nodes_child:
            if node not in visited:
                new_path = path_current[:]
                new_path.append(node)
                paths.append(new_path)
                # To avoid backtracking
                visited.add(node)
        # Continue to next path in list
        path_idx += 1
    # No path is found
    return []

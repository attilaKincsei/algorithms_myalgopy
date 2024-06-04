
"""
Source: https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150

45. Jump Game II
Solved
Medium
Topics
Companies
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].

"""


def create_graph(nums):
    graph = dict()
    for idx, number in enumerate(nums):
        graph[idx] = list(range(min([len(nums) - 1, idx + 1]), min(len(nums), idx + 1 + number)))
    return graph


def jump(nums: list[int]) -> int:
    if len(nums) == 1:
        return 0
    graph = create_graph(nums)
    node_source = 0
    node_target = len(nums) - 1
    visited = {node_source}
    path_idx = 0
    paths = [[node_source]]
    while path_idx < len(paths):
        path_current = paths[path_idx]
        node_current = path_current[-1]
        nodes_child = graph.get(node_current)
        if node_target in nodes_child:
            path_current.append(node_target)
            return len(path_current) - 1
        for node in nodes_child:
            if node not in visited:
                new_path = path_current[:]
                new_path.append(node)
                paths.append(new_path)
                visited.add(node)
        path_idx += 1
    return None


def main():
    test_input4 = [6, 2, 6, 1, 7, 9, 3, 5, 3, 7, 2, 8]
    # return create_graph(test_input4)
    return jump(test_input4)


if __name__ == '__main__':
    print(main())

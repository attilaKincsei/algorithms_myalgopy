

def trap(terrain: list) -> int:
    water = 0
    terrain_max_left = max(terrain)
    terrain_max_idx_left = terrain.index(terrain_max_left)
    terrain_left = terrain[0:terrain_max_idx_left]
    running_max = 0
    if len(terrain_left) > 1:
        for num in terrain_left:
            if num > running_max:
                running_max = num
            water += running_max - num
    terrain_reversed = list(reversed(terrain))
    terrain_max_right = max(terrain_reversed)
    terrain_max_idx_right = terrain_reversed.index(terrain_max_right)
    terrain_right = terrain_reversed[0:terrain_max_idx_right]
    running_max = 0
    if len(terrain_right) > 1:
        for num in terrain_right:
            if num > running_max:
                running_max = num
            water += running_max - num
    terrain_middle = terrain[terrain_max_idx_left:] if 0 == terrain_max_idx_right else terrain[terrain_max_idx_left:terrain_max_idx_right * -1]
    if (terrain_max_left == terrain_max_right) and (len(terrain_middle) > 2):
        for num in terrain_middle:
            water += terrain_max_left - num
    return water


if __name__ == '__main__':
    # input_terrain = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    input_terrain = [4, 2, 3]
    # print(input_terrain[0:])
    print(trap(input_terrain))

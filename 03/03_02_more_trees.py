################################################################################
#
#   Determine the number of trees you would encounter if, for each of the 
#   following slopes, you start at the top-left corner and traverse the map all 
#   the way to the bottom:
#
#       Right 1, down 1.
#       Right 3, down 1. (This is the slope you already checked.)
#       Right 5, down 1.
#       Right 7, down 1.
#       Right 1, down 2.
#
#    What do you get if you multiply together the number of trees encountered 
#    on each of the listed slopes?
#
################################################################################

def has_tree_at(map, row, col):
    col = col % len(map[row])
    return map[row][col] == "#"


def count_trees(map, right_step, down_step):
    count, i, j = 0, 0, 0

    while i < len(map):
        if has_tree_at(map, i, j):
            count += 1
        j += right_step
        i += down_step
    return count

with open("input.txt") as f:
    area_map = f.read().split()
    path_1_1 = count_trees(area_map, 1, 1)
    path_3_1 = count_trees(area_map, 3, 1)
    path_5_1 = count_trees(area_map, 5, 1)
    path_7_1 = count_trees(area_map, 7, 1)
    path_1_2 = count_trees(area_map, 1, 2)
    print(path_1_1 * path_3_1 * path_5_1 * path_7_1 * path_1_2)


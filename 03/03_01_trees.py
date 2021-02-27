################################################################################
#
#   Starting at the top-left corner of your map and following a slope of right 3 
#   and down 1, how many trees would you encounter?
#
################################################################################
import pytest

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


test_data = [
".##",
"...",
"#.#"]
def test_has_tree_at_can_find_tree():
    assert not has_tree_at(test_data, 0, 0)
    assert has_tree_at(test_data, 2, 0)
    assert has_tree_at(test_data, 2, 5)
    assert not has_tree_at(test_data, 1, 923)


example_test = [
    "..##.........##.........##.........##.........##.........##.......",
    "#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..",
    ".#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.",
    "..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#",
    ".#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.",
    "..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....",
    ".#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#", 
    ".#........#.#........#.#........#.#........#.#........#.#........#", 
    "#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...", 
    "#...##....##...##....##...##....##...##....##...##....##...##....#",
    ".#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#"
]

def test_count_trees_matches_example():
    assert count_trees(example_test, 3, 1) == 7



with open("input.txt") as f:
    area_map = f.read().split()
    print(count_trees(area_map, 3, 1))

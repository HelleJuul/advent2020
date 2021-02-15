import pytest

test_data = [1721, 979, 366, 299, 675, 1456]


def find_2020_triplet(data):
    for index1, e1 in enumerate(data):
        for index2, e2 in enumerate(data[index1: ]):
            diff = 2020 - e1 - e2
            if diff in data[index2:]:
                return e1, e2, diff
    return None


def test_ignores_empty_lists():
    assert find_2020_triplet([]) == None

def test_ignores_one_element_lists():
    assert  find_2020_triplet([1]) == None

def test_finds_legal_2020_pair():
    assert find_2020_triplet([2016, 3, 1]) == (2016, 3, 1)
    assert find_2020_triplet([2010, 9, 234, 43, 1]) == (2010, 9, 1)
    assert find_2020_triplet(test_data) == (979, 366, 675)

input_data = []
with open('input.txt') as f:
    for line in f:
        input_data.append(int(line.strip()))

triplet = find_2020_triplet(input_data)
print(triplet[0] * triplet[1] * triplet[2])
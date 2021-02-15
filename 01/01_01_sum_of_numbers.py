import pytest

'''You to find the two entries that sum to 2020 and then multiply those two 
numbers together.'''

test_data = [1721, 979, 366, 299, 675, 1456]


def find_2020_sum_pair(data):
    '''
    Finds two numbers in the input list that sum to 2020
    '''
    for entry in data:
        diff = 2020 - entry
        if diff in data:
            return (entry, diff)
    return None


def fix_expense_report(data):
    pair = find_2020_sum_pair(data)
    if pair is not None:
        return pair[0] * pair[1]
    return None

def test_expense_report_returns_expected():
    assert fix_expense_report(test_data) == 514579

def test_returns_none_when_no_pairs_found():
    assert fix_expense_report([1, 2, 3, 4, 5]) == None

def test_ignores_empty_lists():
    assert fix_expense_report([]) == None

def test_ignores_one_element_lists():
    assert  fix_expense_report([1]) == None

def test_finds_legal_2020_pair():
    assert find_2020_sum_pair([2019, 1]) == (2019, 1)
    assert find_2020_sum_pair([2019, 34, 234, 43, 1]) == (2019, 1)
    assert find_2020_sum_pair(test_data) == (1721, 299)

input_data = []
with open('input.txt') as f:
    for line in f:
        input_data.append(int(line.strip()))

print(fix_expense_report(input_data))


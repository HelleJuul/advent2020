################################################################################
#   
#   To try to debug the problem, they have created a list (your puzzle input) 
#   of passwords (according to the corrupted database) and the corporate policy 
#   when that password was set.
#
#   For example, suppose you have the following list:
#
#   1-3 a: abcde
#   1-3 b: cdefg
#   2-9 c: ccccccccc
#   Each line gives the password policy and then the password. The password 
#   policy indicates the lowest and highest number of times a given letter must 
#   appear for the password to be valid. For example, 1-3 a means that the 
#   password must contain a at least 1 time and at most 3 times.
#
#   In the above example, 2 passwords are valid. The middle password, cdefg, is 
#   not; it contains no instances of b, but needs at least 1. The first and 
#   third passwords are valid: they contain one a or nine c, both within the 
#   limits of their respective policies.
#
#   How many passwords are valid according to their policies?
#
################################################################################

import pytest

test_data = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']


def validate_password(entry):
    bounds, expected_character, password = entry.split()
    lower_bound, upper_bound = bounds.split('-')
    expected_character = expected_character[0] # Remove :

    occurances = password.count(expected_character)

    return int(lower_bound) <= occurances <= int(upper_bound)


def count_valid_passwords(data):
    valid_passwords = filter(validate_password, data)
    return len(list(valid_passwords))


def test_empty_list():
    assert count_valid_passwords([]) == 0

def test_test_input():
    assert count_valid_passwords(test_data) == 2

def test_valid_passwords():
    assert validate_password('1-3 a: a')
    assert validate_password('11-13 x: xxxxxxxxxxjxx')

def test_invalid_passwords():
    assert not validate_password('1-3 a: aaaa')
    assert not validate_password('11-13 x: xxxxxjxlakx')


input_data = []
with open('input.txt') as f:
    input_data = f.readlines()

print(count_valid_passwords(input_data))



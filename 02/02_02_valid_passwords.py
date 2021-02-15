################################################################################
# Each policy actually describes two positions in the password, where 1 means 
# the first character, 2 means the second character, and so on. (Be careful; 
# Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of 
# these positions must contain the given letter. Other occurrences of the letter 
# are irrelevant for the purposes of policy enforcement.
# 
# Given the same example list from above:
# 
# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to the new interpretation of the 
# policies?
################################################################################

import pytest


test_data = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']

def validate_password(entry):
    indexes, expected_character, password = entry.split()
    first_index, second_index = indexes.split('-')
    expected_character = expected_character[0] # Remove :

    match_at_index1 = password[int(first_index) - 1] == expected_character
    match_at_index2 = password[int(second_index) - 1] == expected_character
    
    return (match_at_index1 and not match_at_index2) or (not match_at_index1 and match_at_index2)


def count_valid_passwords(data):
    valid_passwords = filter(validate_password, data)
    return len(list(valid_passwords))



def test_valid_password():
    assert validate_password(test_data[0])


def test_invalid_passwords():
    assert not validate_password(test_data[1])
    assert not validate_password(test_data[2])


def test_correct_count_of_passwords():
    assert count_valid_passwords(test_data) == 1


input_data = []
with open('input.txt') as f:
    input_data = f.readlines()

print(count_valid_passwords(input_data))


import pytest


test_data = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

def test_can_split_into_passports():
    passports = split_input(test_data)
    assert len(passports) == 4

def test_classifies_passport_with_all_fields_as_valid():
    passports = split_input(test_data)
    assert is_valid(passports[0])

def test_classifies_passport_with_only_cid_missing_as_valid():
    passports = split_input(test_data)
    assert is_valid(passports[2])    

def test_classifies_passport_with_missing_field_as_invalid():
    passports = split_input(test_data)
    assert not is_valid(passports[1])
    assert not is_valid(passports[3])

def test_counts_correct_number_of_valid_passports():
    assert count_valid_passports(test_data) == 2



def split_input(data):
    return data.split("\n\n")

def is_valid(passport_data):
    fields = passport_data.split()
    return len(fields) == 8 or (len(fields) == 7 and "cid" not in passport_data)

def count_valid_passports(passport_data):
    passports = split_input(passport_data)
    count = 0
    for passport in passports:
        if is_valid(passport):
            count += 1
    return count




with open('input.txt') as f:
    data = f.read()



print(count_valid_passports(data))


    












  





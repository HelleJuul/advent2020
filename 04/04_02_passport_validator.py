import pytest

################################################################################
#                                                                              #
# A class for passports with a method for checking if it is a valid passport.  #
#                                                                              #
################################################################################

class Passport:

    def __init__(self, passport_data):
        # each passport contains a dict with the passport data
        self.data = {}
        # split into fields
        fields = passport_data.split()
        # for each field split to key:value
        for field in fields:
            key, value = field.split(":")
            self.data[key] = value

    def is_valid(self):
        ''' Return True if the passport is valid. '''
        return self.has_correct_fields() and self.validate_byr() \
                                           and self.validate_iyr() \
                                           and self.validate_eyr() \
                                           and self.validate_hgt() \
                                           and self.validate_hcl() \
                                           and self.validate_ecl() \
                                           and self.validate_pid() \
                                           and self.validate_cid()

    def has_correct_fields(self):
        ''' Return True if all 8 fields are present or if only missing field is
        country id (cid). '''
        return len(self.data) == 8 or \
              (len(self.data) == 7 and "cid" not in self.data.keys())


    def validate_byr(self):
        ''' (Birth Year) - four digits; at least 1920 and at most 2002.'''
        value = self.data.get("byr", -1)
        if value.isnumeric():
            return 1920 <= int(value) <= 2002
        else:
            return False

    def validate_iyr(self):
        ''' (Issue Year) - four digits; at least 2010 and at most 2020. '''
        value = self.data.get("iyr", -1)
        if value.isnumeric():
            return 2010 <= int(value) <= 2020
        else:
            return False

    def validate_eyr(self):
        ''' (Expiration Year) - four digits; at least 2020 and at most 2030. '''
        value = self.data.get("eyr", -1)
        if value.isnumeric():
            return 2020 <= int(value) <= 2030
        else:
            return False

    def validate_hgt(self):
        ''' (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.'''
        value = self.data.get("hgt", -1)
        if "cm" in value:
            value = value.strip("cm")
            return 150 <= int(value) <= 193
        elif "in" in value:
            value = value.strip("in")
            return 59 <= int(value) <= 76
        return False

    def validate_hcl(self):
        ''' (Hair Color) - a # followed by exactly six characters 0-9 or a-f.'''
        value = self.data.get("hcl", -1)
        if len(value) == 7 and value[0] == "#":
            i = 1
            while i < 7:
                if value[i] not in "abcdef0123456789":
                    return False
                i += 1
            return True
        else:
            return False

    def validate_ecl(self):
        ''' (Eye Color) - exactly one of: amb blu brn gry grn hzl oth. '''
        value = self.data.get("ecl", -1)
        return (value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

    def validate_pid(self):
        ''' (Passport ID) - a nine-digit number, including leading zeroes. '''
        value = self.data.get("pid", -1)
        return len(value) == 9 and value.isnumeric()

    def validate_cid(self):
        ''' (Country ID) - ignored, missing or not. '''
        return True


#==============================================================================#
#                                                                              #
#    T E S T I N G                                                             #
#                                                                              #
#==============================================================================#

def test_passport_can_validate_byr():
    passport = Passport("byr:1920")
    assert passport.validate_byr()

    passport = Passport("byr:1919")
    assert not passport.validate_byr()

    passport = Passport("byr:2002")
    assert passport.validate_byr()

    passport = Passport("byr:2003")
    assert not passport.validate_byr()


def test_passport_can_validate_iyr():
    passport = Passport("iyr:2010")
    assert passport.validate_iyr()

    passport = Passport("iyr:2009")
    assert not passport.validate_iyr()

    passport = Passport("iyr:2020")
    assert passport.validate_iyr()

    passport = Passport("iyr:2021")
    assert not passport.validate_iyr()


def test_passport_can_validate_eyr():
    passport = Passport("eyr:2020")
    assert passport.validate_eyr()

    passport = Passport("eyr:2019")
    assert not passport.validate_eyr()

    passport = Passport("eyr:2030")
    assert passport.validate_eyr()

    passport = Passport("eyr:2031")
    assert not passport.validate_eyr()


def test_passport_can_validate_hgt():
    passport = Passport("hgt:150cm")
    assert passport.validate_hgt()

    passport = Passport("hgt:193cm")
    assert passport.validate_hgt()

    passport = Passport("hgt:149cm")
    assert not passport.validate_hgt()

    passport = Passport("hgt:194cm")
    assert not passport.validate_hgt()

    passport = Passport("hgt:59in")
    assert passport.validate_hgt()

    passport = Passport("hgt:76in")
    assert passport.validate_hgt()

    passport = Passport("hgt:58in")
    assert not passport.validate_hgt()

    passport = Passport("hgt:77in")
    assert not passport.validate_hgt()        


def test_passport_can_validate_hcl():
    passport = Passport("hcl:#123af9")
    assert passport.validate_hcl()

    passport = Passport("hcl:123af9")
    assert not passport.validate_hcl()

    passport = Passport("hcl:#123af")
    assert not passport.validate_hcl()

    passport = Passport("hcl:#123afg")
    assert not passport.validate_hcl()   


def test_passport_can_validate_ecl():
    passport = Passport("ecl:amb")
    assert passport.validate_ecl()

    passport = Passport("ecl:blu")
    assert passport.validate_ecl()

    passport = Passport("ecl:brn")
    assert passport.validate_ecl()

    passport = Passport("ecl:gry")
    assert passport.validate_ecl()

    passport = Passport("ecl:grn")
    assert passport.validate_ecl()

    passport = Passport("ecl:hzl")
    assert passport.validate_ecl()

    passport = Passport("ecl:oth")
    assert passport.validate_ecl()

    passport = Passport("ecl:other")
    assert not passport.validate_ecl()


def test_passport_can_validate_pid():
    passport = Passport("pid:123456789")
    assert passport.validate_pid()

    passport = Passport("pid:12345678")
    assert not passport.validate_pid()

    passport = Passport("pid:1234567899")
    assert not passport.validate_pid()

    passport = Passport("pid:abcdefghi")
    assert not passport.validate_pid()


def test_passport_can_validate_cid():
    passport = Passport("")
    assert passport.validate_cid()

    passport = Passport("cid:Denmark")
    assert passport.validate_cid()


################################################################################
#                                                                              #
#   Processing the input and getting the result.                               #
#                                                                              #
################################################################################

def validate_passports():
    ''' Count the number of valid passports in "input.txt" '''
    with open('input.txt') as f:
        data = f.read()
    dataset = data.split("\n\n")
    count = 0
    for entry in dataset:
        passport = Passport(entry)
        if passport.is_valid():
            count += 1
    return count



print(validate_passports())





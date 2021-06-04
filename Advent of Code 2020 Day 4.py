passports = open('Advent of Code 2020 Day 4.txt')
passports = passports.read()
passportdata = passports.split('\n')
# Separating out passport data

fields = ['byr' , 'iyr' , 'eyr' , 'hgt' , 'hcl' , 'ecl' , 'pid']
# Add 'cid' later if needed

def validate(pp):
    for field in fields:
        if field not in pp:
            return False

    return True

validpassports = 0
validpassportdata = []
passport = ''


for data in passportdata:
    if data != '':
        passport += ' ' + data

    else:
        if validate(passport):
            validpassports += 1
            validpassportdata.append(passport)
        passport = ''

if validate(passport):
    validpassports += 1
    validpassportdata.append(passport)
# Tests the last line which has no '' to test

print(validpassports)

# Part 2

def valid_byr(byr):
    byr = int(byr)

    if byr < 1920 or byr > 2002:
        return False

    return True

def valid_iyr(iyr):
    iyr = int(iyr)

    if iyr < 2010 or iyr > 2020:
        return False

    return True

def valid_eyr(eyr):
    eyr = int(eyr)

    if eyr < 2020 or eyr > 2030:
        return False

    return True

def valid_hgt(hgt):
    unit = hgt[-2:]

    if unit not in ['in', 'cm']:
        return False

    hgt = int(hgt[:-2])

    if unit == 'in':
        if hgt < 59 or hgt > 76:
            return False

    if unit == 'cm':
        if hgt < 150 or hgt > 193:
            return False

    return True

def valid_hcl(hcl):
    if hcl[0] != "#":
        return False

    if len(hcl) != 7:
        return False

    return True

def valid_ecl(ecl):
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    return True

def valid_pid(pid):
    if len(pid) != 9:
        return False

    return True

def validate_data(good_passports):
    good_passports = good_passports.split()
    valid_data = {}

    for values in good_passports:
        key = values[:3]
        value = values[4:]
        valid_data[key] = value
# All terms 3 letters so :3 starts at start and counts to 3 characters
# All values begin after ':' so 4: begins at first character after :

    if not valid_byr(valid_data['byr']):
        return False

    if not valid_iyr(valid_data['iyr']):
        return False

    if not valid_ecl(valid_data['ecl']):
        return False

    if not valid_hcl(valid_data['hcl']):
        return False

    if not valid_eyr(valid_data['eyr']):
        return False

    if not valid_hgt(valid_data['hgt']):
        return False

    if not valid_pid(valid_data['pid']):
        return False

    return True

validpassportdatacount = 0

for pp in validpassportdata:
    if validate_data(pp):
        validpassportdatacount += 1

print(validpassportdatacount)

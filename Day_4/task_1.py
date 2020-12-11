
def data_extaction():

    data_input = open("/home/alexander/Desktop/WORK/AdvocadeOfCode_2020/Day_4/passports.txt", "r")
    
    all_passports = ""

    for line in data_input:

        all_passports += line

    data_input.close()
    return all_passports


def seperate_passports(all_passports):

    sep_passports = all_passports.split("\n\n")

    return sep_passports


def find_all(string, *args):
    # Find if all arguments are in string

    return all(word in string for word in args)


def collect_valid_pass(sep_passports):

    valid_passports = []
    total_valid = 0

    for num in range(len(sep_passports)):

        if find_all(sep_passports[num], "byr", "iyr", "hgt", "ecl", "eyr", "hcl", "pid"):

            valid_passports.append(sep_passports[num])
            total_valid += 1

    return valid_passports, total_valid


def create_field_list(valid_passports):

    sep2_val_pass = []
    # Create a list of data, of lists of passports
    sep_val_pass = [num.split() for num in valid_passports]
    # Create a kust if kusts if data, of list of passports
    for num in range(len(sep_val_pass)):
        sep2_val_pass.append([num.split(":") for num in sep_val_pass[num]])

    return sep2_val_pass


"""def detect_valid_pass(sep2_val_pass):

    for num in range(len(sep2_val_pass)):
        for num2 in range(len(sep2_val_pass[num])):



    return"""

all_passports = data_extaction()
sep_passports = seperate_passports(all_passports)
valid_passports, total_valid = collect_valid_pass(sep_passports)
create_field_list(valid_passports)

print(total_valid)

# 'hgt:156cm pid:916654189\nbyr:1943 eyr:2022 ecl:amb hcl:#341e13 iyr:2016', 'cid:305 iyr:2013\neyr:2029 hgt:163cm ecl:blu\nhcl:#fffffd pid:944033881\nbyr:1952', 
# 216
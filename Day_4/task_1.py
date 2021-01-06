import re

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

    potential_valid = []

    # Create a list of data, of lists of passports
    sep_val_pass = [num.split() for num in valid_passports]

    # Create a list of lists of data, of list of passports
    for num in range(len(sep_val_pass)):
        potential_valid.append([num.split(":") for num in sep_val_pass[num]])

    return potential_valid


def detect_valid_pass(potential_valid):
    valid = 0


    for num in range(len(potential_valid)):

        # Field paramerts, initiated as False.
        ecl = False
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        pid = False

        for num2 in range(len(potential_valid[num])):

            first_part = potential_valid[num][num2][0]
            second_part = potential_valid[num][num2][1]
            if first_part == "ecl":
                if len(second_part) == 3 and (second_part == "amb" or second_part == "blu" or second_part == "brn" or second_part == "gry" or second_part == "hzl" or second_part == "oth"):
                    ecl = True
            else:
                print("Failed test on ecl")
            if first_part == "byr" and 1920 <= int(second_part) <= 2002:
                byr = True
            else:
                print("Failed test on byr")
            if first_part == "iyr" and 2010 <= int(second_part) <= 2020:
                iyr = True
            else:
                print("Failed test on iyr")
            if first_part == "eyr" and 2020 <= int(second_part) <= 2030:
                eyr = True
            else:
                    print("Failed test on eyr")
            if first_part == "hgt":

                hight_data = re.split("(?<=\\D)(?=\\d)|(?<=\\d)(?=\\D)", second_part)
                if len(hight_data) == 2:

                    if hight_data[1] == "in" and 59 <= int(hight_data[0]) <= 76:
                        hgt = True
                    if hight_data[1] == "cm" and  150 <= int(hight_data[0]) <= 193:
                        hgt = True
                else:
                    print("Failed test on hgt")

            if first_part == "hcl" and len(second_part) == 7 and second_part[0] == "#" and second_part[1:7].isalnum():
                hcl = True
            else:
                    print("Failed test on hcl")
            if first_part == "pid" and len(second_part) == 9 and second_part.isdecimal():
                pid = True 
            else:
                    print("Failed test on pid")

        if ecl and byr and iyr and eyr and hgt and hcl and pid:
            print("We found one", potential_valid[num])
            valid += 1
            print("Total valid: ", valid)




    return valid

all_passports = data_extaction()
sep_passports = seperate_passports(all_passports)
valid_passports, total_valid = collect_valid_pass(sep_passports)
potential_valid = create_field_list(valid_passports)
valid = detect_valid_pass(potential_valid)

 
#print(potential_valid)
#132
#print(total_valid)

print(valid)
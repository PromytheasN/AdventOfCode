import re


def data_extraction():
    # Extract data into 2 lists. Policies and passwords.
    input_path = (r"/home/alexander/Desktop/WORK"
                  r"/AdvocadeOfCode_2020/Day_2/puzzle_input.txt")
    puzzle_input = open(input_path, "r")

    policy = []
    password = []

    for line in puzzle_input:

        split_line = line.split(":")
        policy.append(split_line[0])
        password.append(split_line[1].strip())

    puzzle_input.close()

    return policy, password


def valid_password_1(data_extraction):
    # Count valid passwords.

    loop_count = 0
    valid_pass = 0

    while loop_count < len(policy):

        # Seperate policy into 3 values, min num, max num and letter
        sep_pol = re.findall(r"[\w']+", policy[loop_count])

        if sep_pol[2] in password[loop_count]:
            letter_count = password[loop_count].count(sep_pol[2])

            if int(sep_pol[0]) <= letter_count <= int(sep_pol[1]):
                valid_pass += 1

        loop_count += 1

    return valid_pass


# Part 2
def valid_password_2(data_extraction):
    # Count valid passwords according to new rules.

    loop_count = 0
    valid_pass = 0

    while loop_count < len(policy):
        sep_pol = re.findall(r"[\w']+", policy[loop_count])

        # If policies letter located at the first position defined by policy
        # and not in second position then pass is valid.
        if (sep_pol[2] == password[loop_count][int(sep_pol[0]) - 1] and
                sep_pol[2] != password[loop_count][int(sep_pol[1]) - 1]):
            valid_pass += 1

        # If policies letter located at the second position defined
        # by policy and not in first position then pass is valid.
        elif (sep_pol[2] != password[loop_count][int(sep_pol[0]) - 1] and
                sep_pol[2] == password[loop_count][int(sep_pol[1]) - 1]):
            valid_pass += 1

        loop_count += 1

    return valid_pass


policy, password = data_extraction()
valid_pass_1 = valid_password_1(data_extraction)
valid_pass_2 = valid_password_2(data_extraction)

print(valid_pass_1)
print(valid_pass_2)

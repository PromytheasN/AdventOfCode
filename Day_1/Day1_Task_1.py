target = 2020


def exp_report_input():

    expenses_list = []
    expenses = input("Please insert the list of expenses."
                     "When you are done, insert Q or q to end input. ")

    # When input = Q or q, collecting input is terminated.
    while expenses != 'q' and expenses != 'Q':
        expenses_list.append(int(expenses))
        expenses = input()

    return expenses_list


def find_2_entries(target):

    result_2 = 0

    for num in expenses_list:
        # Filters higher than 2020 numbers
        # As expenses are positive integars.
        if num <= target:
            for num2 in expenses_list:
                if num2 <= target:
                    if num + num2 == target:
                        print("The product of the 2 numbers"
                              " that euals to 2020 are: ")
                        result_2 = num * num2
                        return result_2


def find_3_entries(target):

    result_3 = 0

    for num in expenses_list:
        if num <= target:
            for num2 in expenses_list:
                if num2 <= target:
                    for num3 in expenses_list:
                        if num3 <= target:
                            if num + num2 + num3 == target:
                                print("The product of the 3 numbers"
                                      "that euals to 2020 are: ")
                                result_3 = num * num2 * num3
                                return result_3


expenses_list = exp_report_input()
result_2 = find_2_entries(target)
result_3 = find_3_entries(target)

print(result_2)
print(result_3)

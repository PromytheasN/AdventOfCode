
def data_extraction():
    # Extract data and extends tree map.

    input_path = (r"/home/alexander/Desktop/WORK"
                  r"/AdvocadeOfCode_2020/Day_3/map_input.txt")
    map_input = open(input_path, "r")

    tree_lines = []
    line_count = 1

    for line in map_input:
        line_count += 1
        tree_lines.append(line.strip() * (line_count))

    map_input.close()

    return tree_lines


def count_tree_encounter(tree_lines, right_step, down_step):
    # Calculate tree encounters

    tree_encounters = 0
    position = right_step
    line = down_step

    # While position < than length of last line - right_step + 1 and line within tree_map length
    while line <= len(tree_lines) - down_step:

        print("Current position we are looking and line is: ", position, line)
        if tree_lines[line][position] == "#":
            tree_encounters += 1
            print("we found one more, total: ", tree_encounters)
            print("Line we found it is: ", line + down_step)

        line += down_step
        #print("new line is: ", line)
        position += right_step
        print("new position and line that we are going to look is: ", position, "and", line)
    return tree_encounters


tree_lines = data_extraction()
countr3d1 = count_tree_encounter(tree_lines, 3, 1)
countr1d1 = count_tree_encounter(tree_lines, 1, 1)
print("R1D1 : ", countr1d1)
countr5d1 = count_tree_encounter(tree_lines, 5, 1)
print("R5D1", countr5d1)
countr7d1 = count_tree_encounter(tree_lines, 7, 1)
print("R7D1", countr7d1)
countr1d2 = count_tree_encounter(tree_lines, 1, 2)
print("R1D2", countr1d2)

print("The number of encounters for right 3 down 1 are: ", countr3d1)

product = countr1d1 * countr1d2 * countr3d1 * countr5d1 * countr7d1

print("The product of all encounters is: ", product)

# not 5690521200, 4893848232, 5007658656
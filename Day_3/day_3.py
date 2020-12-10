
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

    # While position < than length of final line - 1
    # and line within tree_map length
    while line <= len(tree_lines) - 1:

        if tree_lines[line][position] == "#":
            tree_encounters += 1

        line += down_step
        position += right_step
    return tree_encounters


tree_lines = data_extraction()

# Assiging all slope patterns
countr3d1 = count_tree_encounter(tree_lines, 3, 1)
countr1d1 = count_tree_encounter(tree_lines, 1, 1)
countr5d1 = count_tree_encounter(tree_lines, 5, 1)
countr7d1 = count_tree_encounter(tree_lines, 7, 1)
countr1d2 = count_tree_encounter(tree_lines, 1, 2)
product = countr1d1 * countr1d2 * countr3d1 * countr5d1 * countr7d1

print("The product of the tree encouters of each listed slope is: ", product)

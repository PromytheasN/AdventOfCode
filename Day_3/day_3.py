
def data_extraction():
    # Extract data and extends tree map.

    input_path = (r"/home/alexander/Desktop/WORK"
                  r"/AdvocadeOfCode_2020/Day_3/map_input.txt")
    map_input = open(input_path, "r")

    tree_lines = []
    line_count = 1

    for line in map_input:

        line_count += 1
        tree_lines.append(line.strip() * line_count)

    map_input.close()

    return tree_lines, line_count


def count_tree_encounter(tree_lines, line_count):

    tree_encounters = 0
    position = 0

    while position <= len(tree_lines[line_count - 2]):

        for line in tree_lines:
            print(line)
            if line[position] == "#":
                tree_encounters += 1
        position += 3

    return tree_encounters


tree_lines, line_count = data_extraction()
count = count_tree_encounter(tree_lines, line_count)

print(count)

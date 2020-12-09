
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


def count_tree_encounter(tree_lines):

    tree_encounters = 0
    position = 3
    line = 1

    # While position < than length of last line - 3 and line within tree_map
    while position <= len(tree_lines[len(tree_lines) - 3]) and line < len(tree_lines):
        
        if tree_lines[line][position] == "#":
            tree_encounters += 1
        line += 1
        position += 3

    return tree_encounters


tree_lines = data_extraction()
count = count_tree_encounter(tree_lines)

print(count)

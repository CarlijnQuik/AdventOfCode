
f = open("Day3_input.txt", "r")

lines = []
for line in f:
    lines.append(line.strip())

f.close()

def find_trees_with_slope(right, down):
    i = down
    tree_counter = 0
    characters_per_line = len(lines[0])
  
    while i < len(lines):
        char_pos = round(((i/down)*right) % characters_per_line)
        if (lines[i][char_pos]) == "#":
            tree_counter += 1

        i += down
  
    return tree_counter

right1_down1 = find_trees_with_slope(1,1)
print(right1_down1)
# Part 1
right3_down1 = find_trees_with_slope(3,1)
print(right3_down1)
right5_down1 = find_trees_with_slope(5,1)
print(right5_down1)
right7_down1 = find_trees_with_slope(7,1)
print(right7_down1)
right1_down2 = find_trees_with_slope(1,2)
print(right1_down2)

# Part 2
total_trees = right1_down1*right3_down1*right5_down1*right7_down1*right1_down2
print(total_trees)
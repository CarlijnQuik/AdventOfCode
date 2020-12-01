from itertools import combinations
f = open("Day1_input.txt", "r")

list_of_numbers = []

for line in f:
    if line:
        list_of_numbers.append(int(line.strip()))

# Part 1
all_combinations = list(combinations(list_of_numbers, 2))
for combination in all_combinations:
    if combination[0] + combination[1] == 2020:
        print(combination[0]*combination[1])

# Part 2
all_combinations = list(combinations(list_of_numbers, 3))
for combination in all_combinations:
    if combination[0] + combination[1] + combination[2] == 2020:
        print(combination[0]*combination[1]*combination[2])

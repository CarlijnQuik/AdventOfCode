from itertools import permutations,combinations,groupby

# Read input
f = open("Day10_input.txt", "r")

# Read and sort input
numbers = []
for number in f:
    numbers.append(int(number.strip()))

f.close()
numbers.sort()

def find_differences(numbers):
    i = 0
    i_previous_number = i
    difference_of_1 = 0
    difference_of_3 = 1
    max_number = numbers[len(numbers)-1]

    while i <= max_number:
        if i in numbers:
            difference = i - i_previous_number
            if difference == 1:
                difference_of_1 += 1
            elif difference == 3:
                difference_of_3 += 1
            i_previous_number = i
            
        i += 1

    return difference_of_1,difference_of_3,difference_of_1*difference_of_3

print("Part 1_1: ",find_differences(numbers)[0])
print("Part 1_3: ",find_differences(numbers)[1])
print("Part 1_m: ",find_differences(numbers)[2])

def count_combinations(gap):
    if gap == 1:
        return 1
    elif gap == 2:
        return 1
    elif gap == 3:
        return 2
    elif gap == 4:
        return 4
    elif gap == 5:
        return 7

def find_combinations(numbers):
    previous_number = 0
    combinations = 1
    gap = 1

    for number in numbers:
        if number - previous_number == 3:
            combinations *= count_combinations(gap)
            gap = 0
        gap += 1
        previous_number = number

    combinations *= count_combinations(gap)
    return combinations

print("Part 2: ",find_combinations(numbers))



      




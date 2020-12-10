import itertools
import numpy as np

# Read input
f = open("Day9_input.txt", "r")

# Read input
numbers = []
for number in f:
    numbers.append(int(number.strip()))

f.close()

def check_sum(number,options):
    for option in options:
        remainder = number - option
        if remainder in options and remainder != number:
            return 1
    return 0

def find_number(preamble):
    i = preamble
    loops = 0
    while i < len(numbers):
        correct_sum = check_sum(numbers[i],numbers[loops:i])
        if correct_sum == 0:
            return numbers[i]
        i += 1
        loops += 1
    
part_1 = find_number(25)
print(numbers)
  
def find_sum(sum_part_1):
    i = 0
    while i < len(numbers):
        sum = 0
        j = i
        while j >= 0:
            # print(sum, numbers[j])
            sum += numbers[j]
            if sum == sum_part_1:
                return i,j
            elif sum > sum_part_1:
                break
            j -= 1
        i += 1

part_2 = find_sum(1504371145)
parts_of_sum = numbers[part_2[1]:part_2[0]+1]
parts_of_sum.sort()
print(parts_of_sum)
print("Smallest element is:", parts_of_sum[0])
print("Largest element is:", parts_of_sum[len(parts_of_sum)-1])
print(parts_of_sum[0] + parts_of_sum[len(parts_of_sum)-1])


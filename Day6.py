import collections
f = open("Day6_input.txt", "r")

groups = []
group = []

def split(word): 
    return [char for char in word]

for line in f:
    # print(line)
    if line == "\n":
        groups.append(group)
        group = []
    else:
        group += split(line)

group += "\n"
groups.append(group)        
f.close()

count_1 = 0
count_2 = 0

for group in groups:
    print("START:")
    number_of_persons = group.count("\n")
    occurrences = collections.Counter(group)
    # print(occurrences)
    for answer in set(group):
        if answer != "\n":
            print("answer",answer)
            print("no",occurrences[answer])
            if occurrences[answer] == number_of_persons:
                count_2 += 1
                print("added")

    # Part 1
    count_1 += (len(set(group))-1)

    # Part 2


print(count_2)



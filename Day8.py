f = open("Day8_input.txt", "r")

# Read input
lines = []
for line in f:
    lines.append(line.strip())
f.close()

# Part 1
def read_instructions(lines):
    i = 0
    acc = 0
    breaked = 0
    ran_lines = []
    while i < len(lines):
        instruction = lines[i].split(" ")[0]
        value = lines[i].split(" ")[1]
    
        if i in ran_lines:
            breaked = 1
            break
        else:
            ran_lines.append(i)
            if instruction == "acc":
                acc += int(value)

            if instruction == "jmp":
                i += int(value)
            else:
                i += 1

    return acc,breaked

def find_bug(lines):
    j = 0
    acc = 0
    while j < len(lines):
        line = lines[j]
        instruction = lines[j].split(" ")[0]
        value = lines[j].split(" ")[1]
        
        if instruction == "jmp":
            lines[j] = "nop " + value
            acc = read_instructions(lines.copy())[0]
            breaked = read_instructions(lines.copy())[1]
            if breaked == 1:
                acc = 0
            lines[j] = line
        elif instruction == "nop":
            lines[j] = "jmp " + value
            acc = read_instructions(lines.copy())[0]
            breaked = read_instructions(lines.copy())[1]
            if breaked == 1:
                acc = 0
            lines[j] = line
        
        j += 1
        if acc > 0:
            break

    return acc

# Part 1
print("part 1: ",read_instructions(lines)[0])
print("part 2: ",find_bug(lines))






    


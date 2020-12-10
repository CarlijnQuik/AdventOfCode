# Read input
f = open("Day5_input.txt", "r")
boarding_passes = []
for boarding_pass in f:
    boarding_passes.append(boarding_pass.strip())
f.close()

def get_seat_ids():
    boarding_pass_seats = {}
    seat_ids = []
    for boarding_pass in boarding_passes:
        min_row = 0
        max_row = int(128)
        min_column = 0
        max_column = int(8)
        for letter in boarding_pass:
            if letter == "F":
                max_row = int((max_row+min_row)/2)
            elif letter == "B":
                min_row = int((max_row+min_row)/2)
            elif letter == "L":
                max_column = int((max_column+min_column)/2)
            elif letter == "R":
                min_column = int((max_column+min_column)/2)
            else:
                break
            
        boarding_pass_seats[(min_row*8)+min_column] = {"row": min_row, "column": min_column, "pass": boarding_pass}
        seat_ids.append((min_row*8)+min_column)
    return boarding_pass_seats,seat_ids

seat_ids = get_seat_ids()[1]
seat_ids.sort()

# print("Part 1: ", seat_ids[len(seat_ids)-1])

def possible_seats():
    row = 1
    max_row = int(126)
    max_column = int(8)
    seat_ids = []
    while row < max_row:
        column = 0
        while column < max_column:
            seat_ids.append((row*8)+column)
            column += 1
        row += 1
    
    return seat_ids

# Part 2
possible_seats = possible_seats()
empty_seat_ids = list(set(possible_seats) - set(seat_ids))

print(empty_seat_ids)




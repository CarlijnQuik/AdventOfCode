# Read input
f = open("Day5_input.txt", "r")
boarding_passes = []
for boarding_pass in f:
    boarding_passes.append(boarding_pass.strip())
f.close()


def determine_seat(boarding_pass):
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
    return {"row": min_row, "column": min_column, "pass": boarding_pass, "id": (min_row*8)+min_column}
    
def get_seat_ids():
    seat_ids = []
    for boarding_pass in boarding_passes:
        seat = determine_seat(boarding_pass)
        seat_ids.append(seat["id"])
    return seat_ids

# Part 1
seat_ids = get_seat_ids()
print("Part 1: ", max(seat_ids))

# Part 2
my_seat = set(range(min(seat_ids), max(seat_ids))) - set(seat_ids)
print(my_seat)




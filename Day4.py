f = open("Day4_input.txt", "r")

passports = []
passport = []

for line in f:
    if line == "\n":
        passports.append(passport)
        passport = []
    else:
        passport += line.split()

passports.append(passport)        
f.close()

required_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
complete_passports = []
for passport in passports:
    fields_in_passport = []
    for field in passport:
        field_name = field.split(":")[0]
        field_value = field.split(":")[1]

        if(field_name != "cid"):
            fields_in_passport.append(field_name)

    if(set(required_fields) == set(fields_in_passport)):
        complete_passports.append(passport)

# Part 1
# print(len(complete_passports))

# Convert list to dictionary
def convert(a):
    d = {}
    for b in a:
        i = b.split(':')
        d[i[0]] = i[1]

    return d

print("passports",len(complete_passports))

correct_passports = 0
for passport in complete_passports:
    correct_fields = 0
    passport = convert(passport)
    print(passport)
 
    # Check birthyear
    # print(passport.get("byr"))
    if(len(passport.get("byr")) == 4 and int(passport.get("byr")) >= 1920 and int(passport.get("byr")) <= 2002):
        # print("valid")
        correct_fields += 1

    # Check issue year
    # print(passport.get("iyr"))
    if(len(passport.get("iyr")) == 4 and int(passport.get("iyr")) >= 2010 and int(passport.get("iyr")) <= 2020):
        correct_fields += 1
        # print("valid")
    
    # Check expiration year
    # print(passport.get("eyr"))
    if(len(passport.get("eyr")) == 4 and int(passport.get("eyr")) >= 2020 and int(passport.get("eyr")) <= 2030):
        correct_fields += 1
        # print("valid")

    # Check height cm
    # print(passport.get("hgt"))
    if passport.get("hgt").endswith("cm") and int(passport.get("hgt").strip("cm")) >= 150 and int(passport.get("hgt").strip("cm")) <= 193:
        correct_fields += 1
        # print("valid cm")

    # Check height in
    if passport.get("hgt").endswith("in") and int(passport.get("hgt").strip("in")) >= 59 and int(passport.get("hgt").strip("in")) <= 76:
        correct_fields += 1
        # print("valid in")

    # Check hair color
    # print(passport.get("hcl"))
    if passport.get("hcl").startswith("#"):
        correct_fields += 1
        for character in passport.get("hcl")[1:]:
            if character not in ["a","b","c","d","e","f","0","1","2","3","4","5","6","7","8","9"]:
                correct_fields -= 1
                # print("invalid")

    # Check eye color
    # print(passport.get("ecl"))
    if passport.get("ecl") in ["amb","blu","brn","gry","grn","hzl","oth"]:
        correct_fields += 1
        # print("valid")

    # Check passport ID
    # print(passport.get("pid"))
    if len(passport.get("pid")) == 9 and passport.get("pid").isnumeric():
        correct_fields += 1
        # print("valid")

    # print("valid fields", correct_fields)
    if(correct_fields == 7):
        correct_passports += 1

print("valid passports",correct_passports)
    
    
    
   
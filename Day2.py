f = open("Day2_input.txt", "r")

list_of_passwords = []
validity_counter_1 = 0
validity_counter_2 = 0

for line in f:
    if line:
        policy = line.split(":")[0]
        password = line.split(":")[1]
        policy_range = policy.split(" ")[0]
        policy_letter = policy.split(" ")[1]
        policy_minimum = int(policy_range.split("-")[0])
        policy_maximum = int(policy_range.split("-")[1])

        # Part 1
        if password.count(policy_letter) >= policy_minimum and password.count(policy_letter) <= policy_maximum:
            validity_counter_1 += 1

        # Part 2
        policy_range_list = [policy_minimum, policy_maximum]
        password_matches = [pos for pos, char in enumerate(password) if char == policy_letter]
        indexes_of_occurence_within_range = set(policy_range_list) & set(password_matches)
        if len(indexes_of_occurence_within_range) == 1:
            validity_counter_2 += 1

print(validity_counter_1)
print(validity_counter_2)


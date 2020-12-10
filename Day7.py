# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.

# In the above rules, the following options would be available to you:
# A bright white bag, which can hold your shiny gold bag directly.
# A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
# A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
# A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
# So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

f = open("Day7_input.txt", "r")

# Read input
lines = []
for line in f:
    lines.append(line.strip())
f.close()

# print(lines)
valid_bags_found = []
for line in lines:
    bag = line.split("contain")[0].split(" ")[:2]
    bag = bag[0] + " " + bag[1]
    
    bags_in_bag = line.split("contain")[1].split(",")

    for bag_in_bag in bags_in_bag:
        if "shiny gold bag" in bag_in_bag:
            valid_bags_found.append(bag)
            print(bag_in_bag,"+1")


for line in lines:
    bag = line.split("contain")[0].split(" ")[:2]
    bag = bag[0] + " " + bag[1]
    
    bags_in_bag = line.split("contain")[1].split(",")

    for bag_in_bag in bags_in_bag:
        print(valid_bags_found)
        bag_to_check = bag_in_bag.split(" ")[2] + " " + bag_in_bag.split(" ")[3]
        print(bag_to_check)
        # print(valid_bags_found,bag_to_check)
        if bag_to_check in valid_bags_found:
            print(bag_in_bag,"+1")
            valid_bags_found.append(bag)

    print(set(valid_bags_found))
    print(len(set(valid_bags_found)))




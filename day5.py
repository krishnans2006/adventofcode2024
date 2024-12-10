constraints = []
updates = []

with open("day5.txt", "r") as file:
    on_constraints = True

    for line in file:
        if line.strip() == "":
            on_constraints = False
            continue

        if on_constraints:
            constraints.append(tuple(int(p) for p in line.strip().split("|")))
        else:
            updates.append([int(l) for l in line.strip().split(",")])

sum_of_middle_numbers = 0

for update in updates:
    is_valid = True

    for constraint in constraints:
        if constraint[0] not in update or constraint[1] not in update:
            continue
        index1 = update.index(constraint[0])
        index2 = update.index(constraint[1])
        if index1 > index2:
            is_valid = False
            break

    if is_valid:
        sum_of_middle_numbers += update[len(update) // 2]

print(sum_of_middle_numbers)

sum_of_middle_numbers = 0

for update in updates:
    is_valid = True

    for constraint in constraints:
        if constraint[0] not in update or constraint[1] not in update:
            continue
        index1 = update.index(constraint[0])
        index2 = update.index(constraint[1])
        if index1 > index2:
            is_valid = False
            break

    if not is_valid:
        for _ in range(len(update)):
            for constraint in constraints:
                if constraint[0] not in update or constraint[1] not in update:
                    continue
                index1 = update.index(constraint[0])
                index2 = update.index(constraint[1])
                if index1 > index2:
                    update[index1], update[index2] = update[index2], update[index1]

        sum_of_middle_numbers += update[len(update) // 2]

print(sum_of_middle_numbers)

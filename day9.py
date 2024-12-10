with open("day9.txt", "r") as file:
    filesystem_input = "".join([line.strip() for line in file])

filesystem = []
current_file_id = 0
for i, char in enumerate(filesystem_input):
    if i % 2 == 0:  # file
        filesystem.extend([current_file_id] * int(char))
        current_file_id += 1
    else:  # free space
        filesystem.extend([-1] * int(char))


pointer_left = 0
pointer_right = len(filesystem) - 1

while pointer_left < pointer_right:
    if filesystem[pointer_left] != -1:
        pointer_left += 1
        continue
    if filesystem[pointer_right] == -1:
        pointer_right -= 1
        continue

    filesystem[pointer_left], filesystem[pointer_right] = filesystem[pointer_right], filesystem[pointer_left]

checksum = 0
for i, file in enumerate(filesystem):
    if file == -1:
        break
    checksum += i * file

print(checksum)


filesystem = []
current_file_id = 0
for i, char in enumerate(filesystem_input):
    if i % 2 == 0:  # file
        filesystem.append((current_file_id, int(char)))
        current_file_id += 1
    else:  # free space
        filesystem.append((-1, int(char)))


pointer_left = 0
pointer_right = len(filesystem) - 1

while pointer_right > 1:
    while pointer_left < pointer_right:
        if filesystem[pointer_left][0] != -1:
            pointer_left += 1
            continue
        if filesystem[pointer_right][0] == -1:
            pointer_right -= 1
            continue

        if filesystem[pointer_left][1] < filesystem[pointer_right][1]:
            pointer_left += 1
            continue
        if filesystem[pointer_left][1] == filesystem[pointer_right][1]:
            filesystem[pointer_left], filesystem[pointer_right] = filesystem[pointer_right], filesystem[pointer_left]
            continue
        if filesystem[pointer_left][1] > filesystem[pointer_right][1]:
            old_pointer_right = filesystem[pointer_right]
            old_pointer_left = filesystem[pointer_left]
            filesystem[pointer_left] = old_pointer_right
            filesystem[pointer_right] = (-1, old_pointer_right[1])
            filesystem.insert(pointer_left + 1, (-1, old_pointer_left[1] - old_pointer_right[1]))
            pointer_left += 1
            pointer_right += 1
            continue
    pointer_left = 0
    pointer_right -= 1

# print(filesystem)

checksum = 0
position = 0
for i, (id_, count) in enumerate(filesystem):
    if id_ == -1:
        position += count
        continue
    for j in range(position, position + count):
        checksum += j * id_
    position += count

print(checksum)

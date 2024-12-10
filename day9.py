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

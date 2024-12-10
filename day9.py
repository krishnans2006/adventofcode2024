import tqdm
import tqdm.contrib

with open("day9test.txt", "r") as file:
    filesystem_input = "".join([line.strip() for line in file])

filesystem = ""
current_file_id = 0
for i, char in enumerate(filesystem_input):
    if i % 2 == 0:  # file
        filesystem += str(current_file_id) * int(char)
        current_file_id += 1
    else:  # free space
        filesystem += "." * int(char)

final_file_id = 0
for i in tqdm.trange(len(filesystem)):
    if len(set(filesystem[i:])) == 1:  # only free space left
        final_file_id = i - 1
        break

    if filesystem[i] == ".":
        for j in range(len(filesystem) - 1, -1, -1):
            if filesystem[j] != ".":
                filesystem = filesystem[:i] + filesystem[j] + filesystem[i + 1:j] + "." + filesystem[j + 1:]
                break

checksum = 0
for i, file in tqdm.contrib.tenumerate(filesystem[:final_file_id + 1]):
    checksum += i * int(file)

print(checksum, filesystem)

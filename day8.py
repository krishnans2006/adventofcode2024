from itertools import combinations

grid = ""

with open("day8.txt", "r") as file:
    width = 0
    for line in file:
        grid += line.strip()
        if width == 0:
            width = len(line.strip())
    height = len(grid) // width


def grid_print(grid):
    for i in range(0, len(grid), width):
        print(grid[i:i + width])
    print()


frequencies = set(grid) - {"."}

antinodes = set()

for frequency in frequencies:
    if grid.count(frequency) < 2:
        continue

    frequency_indices = [i for i, x in enumerate(grid) if x == frequency]
    frequency_index_combinations = list(combinations(frequency_indices, 2))

    for (f1, f2) in frequency_index_combinations:
        del_x = f1 % width - f2 % width
        del_y = f1 // width - f2 // width
        if not (f1 % width) + del_x >= width and not (f1 % width) + del_x < 0 and not f1 + del_x + del_y * width >= width * height and not f1 + del_x + del_y * width < 0:
            new_antinode_1 = f1 + del_x + del_y * width
            antinodes.add(new_antinode_1)
            # print(f1, f2, new_antinode_1)
        if not (f2 % width) - del_x >= width and not (f2 % width) - del_x < 0 and not f2 - (del_x + del_y * width) >= width * height and not f2 - (del_x + del_y * width) < 0:
            new_antinode_2 = f2 - (del_x + del_y * width)
            antinodes.add(new_antinode_2)
            # print(f1, f2, new_antinode_2)

# new_grid = "." * width * height
# for i in antinodes:
#     new_grid = new_grid[:i] + "#" + new_grid[i + 1:]
# grid_print(new_grid)

print(len(antinodes))


antinodes = set()

for frequency in frequencies:
    if grid.count(frequency) < 2:
        continue

    frequency_indices = [i for i, x in enumerate(grid) if x == frequency]
    frequency_index_combinations = list(combinations(frequency_indices, 2))

    for (f1, f2) in frequency_index_combinations:
        antinodes.update({f1, f2})

        del_x = f1 % width - f2 % width
        del_y = f1 // width - f2 // width

        antinode_1s = set()
        k1 = f1 + del_x + del_y * width
        k1_x = (f1 % width) + del_x
        k1_y = (f1 // width) + del_y
        while not k1_x >= width and not k1_x < 0 and not k1 >= width * height and not k1 < 0:
            antinode_1s.add(k1)
            k1 = k1 + del_x + del_y * width
            k1_x += del_x
            k1_y += del_y
        antinodes.update(antinode_1s)

        antinode_2s = set()
        k2 = f2 - (del_x + del_y * width)
        k2_x = (f2 % width) - del_x
        k2_y = (f2 // width) - del_y
        while not k2_x >= width and not k2_x < 0 and not k2 >= width * height and not k2 < 0:
            antinode_2s.add(k2)
            k2 = k2 - (del_x + del_y * width)
            k2_x -= del_x
            k2_y -= del_y
        antinodes.update(antinode_2s)


# new_grid = "." * width * height
# for i in antinodes:
#     new_grid = new_grid[:i] + "#" + new_grid[i + 1:]
# grid_print(new_grid)

print(len(antinodes))

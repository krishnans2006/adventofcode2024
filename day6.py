import tqdm

grid = ""

with open("day6.txt", "r") as file:
    width = 0
    for line in file:
        grid += line.strip()
        if width == 0:
            width = len(line.strip())
    height = len(grid) // width

original_grid = grid


def grid_print(grid):
    for i in range(0, len(grid), width):
        print(grid[i:i + width])
    print()


guard_move_offsets = {
    "^": -width,
    ">": 1,
    "v": width,
    "<": -1
}

guard_move_oob = {
    "^": lambda x: x < 0,
    ">": lambda x: x % width == 0,
    "v": lambda x: x >= width * height,
    "<": lambda x: x % width == width - 1
}

guard_char_after_turn = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
}

visited_cells = set()

while True:
    # grid_print(grid)
    if "^" in grid:
        guard_char = "^"
    elif ">" in grid:
        guard_char = ">"
    elif "v" in grid:
        guard_char = "v"
    elif "<" in grid:
        guard_char = "<"
    else:
        break

    guard_index = grid.index(guard_char)
    visited_cells.add(guard_index)

    next_pos = guard_index + guard_move_offsets[guard_char]

    if guard_move_oob[guard_char](next_pos):
        break

    if grid[next_pos] == "#":
        new_guard_char = guard_char_after_turn[guard_char]
        grid = grid.replace(guard_char, new_guard_char, 1)
    else:
        grid = grid.replace(guard_char, ".", 1)
        grid = grid[:next_pos] + guard_char + grid[next_pos + 1:]

print(len(visited_cells))

grid = original_grid
ways_stuck_in_loop = 0

for i in tqdm.trange(len(grid)):
    if grid[i] == "#":
        continue
    new_grid = grid[:i] + "#" + grid[i + 1:]

    positions_reached = set()  # (r, c, char)
    is_stuck_in_loop = False

    while True:
        if "^" in new_grid:
            guard_char = "^"
        elif ">" in new_grid:
            guard_char = ">"
        elif "v" in new_grid:
            guard_char = "v"
        elif "<" in new_grid:
            guard_char = "<"
        else:
            break

        guard_index = new_grid.index(guard_char)
        position_reached = (guard_index // width, guard_index % width, guard_char)
        if position_reached in positions_reached:
            is_stuck_in_loop = True
            break
        positions_reached.add(position_reached)

        next_pos = guard_index + guard_move_offsets[guard_char]

        if guard_move_oob[guard_char](next_pos):
            break

        if new_grid[next_pos] == "#":
            new_guard_char = guard_char_after_turn[guard_char]
            new_grid = new_grid.replace(guard_char, new_guard_char, 1)
        else:
            new_grid = new_grid.replace(guard_char, ".", 1)
            new_grid = new_grid[:next_pos] + guard_char + new_grid[next_pos + 1:]

    if is_stuck_in_loop:
        ways_stuck_in_loop += 1

print(ways_stuck_in_loop)

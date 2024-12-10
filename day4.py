import re

with open("day4.txt", "r") as file:
    lines = file.readlines()

    width = len(lines[0].strip())
    height = len(lines)

    puzzle = "".join([l.strip() for l in lines])


count = 0

# Rows
for r in range(height):
    row = puzzle[r*width:(r+1)*width]
    count += row.count("XMAS") + row.count("SAMX")

# Columns
for r in range(width):
    col = puzzle[r::width]
    count += col.count("XMAS") + col.count("SAMX")

# Diagonals
for r in range(width + height - 1):
    main_diag = ""
    for i in range(r + 1):
        if i < height and r - i < width:
            main_diag += puzzle[i * width + r - i]
    count += main_diag.count("XMAS") + main_diag.count("SAMX")

    off_diag = ""
    for i in range(r + 1):
        if i < height and r - i < width:
            off_diag += puzzle[i * width + width - r + i - 1]
    count += off_diag.count("XMAS") + off_diag.count("SAMX")

print(count)


count = 0

for r in range(height - 2):
    for c in range(width - 2):
        # X shape
        relevant_chars = puzzle[r*width + c] + puzzle[r*width + c + 2] + puzzle[(r+1)*width + c + 1] + puzzle[(r+2)*width + c] + puzzle[(r+2)*width + c + 2]

        if relevant_chars in ("MMASS", "SMASM", "SSAMM", "MSAMS"):
            count += 1

print(count)

import re

with open("day3.txt", "r") as file:
    input_string = "".join(file.readlines())

# language=regexp
pattern = r"mul\((\d+),(\d+)\)"

matches = re.findall(pattern, input_string)

result = 0

for match in matches:
    result += int(match[0]) * int(match[1])

print(result)


new_input_string = "do()" + input_string + "do()"

# language=regexp
bad_patterns = r"don't\(\).*?do\(\)"

bad_matches = re.findall(bad_patterns, new_input_string, flags=re.DOTALL)

for bad_match in bad_matches:
    new_input_string = new_input_string.replace(bad_match, "")

result = 0

for match in re.findall(pattern, new_input_string):
    result += int(match[0]) * int(match[1])

print(result)

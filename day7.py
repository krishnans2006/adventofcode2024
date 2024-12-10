import itertools
import tqdm

equations = []

with open("day7.txt", "r") as file:
    for line in file:
        answer, numbers = line.strip().split(": ")
        equations.append((int(answer), [int(x) for x in numbers.split()]))


operator_eval = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
}

total_result = 0


for answer, numbers in equations:
    num_numbers = len(numbers)
    num_operators = num_numbers - 1

    operator_permutations = list(itertools.product(("+", "*"), repeat=num_operators))

    for perm in operator_permutations:
        new_numbers = numbers.copy()
        for i in range(len(new_numbers) - 1):
            next_operator = perm[-1]
            perm = perm[:-1]
            new_numbers[i + 1] = operator_eval[next_operator](new_numbers[i], new_numbers[i + 1])
        computed_answer = new_numbers[-1]

        if computed_answer == answer:
            total_result += answer
            break

print(total_result)

operator_eval["|"] = lambda x, y: x * (10 ** len(str(y))) + y

total_result = 0

for answer, numbers in tqdm.tqdm(equations):
    num_numbers = len(numbers)
    num_operators = num_numbers - 1

    operator_permutations = list(itertools.product(("+", "*", "|"), repeat=num_operators))

    for perm in operator_permutations:
        new_numbers = numbers.copy()
        for i in range(len(new_numbers) - 1):
            next_operator = perm[-1]
            perm = perm[:-1]
            new_numbers[i + 1] = operator_eval[next_operator](new_numbers[i], new_numbers[i + 1])
        computed_answer = new_numbers[-1]

        if computed_answer == answer:
            total_result += answer
            break

print(total_result)

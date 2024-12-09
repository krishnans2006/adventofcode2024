list1 = []
list2 = []

with open("day1.txt", "r") as file:
    for line in file:
        num1, num2 = line.strip().split()
        list1.append(int(num1))
        list2.append(int(num2))

list1.sort()
list2.sort()

total_distance = 0

for (num1, num2) in zip(list1, list2):
    total_distance += abs(num1 - num2)

print(total_distance)

similarity_score = 0

for num1 in list1:
    count = list2.count(num1)
    similarity_score += num1 * count

print(similarity_score)

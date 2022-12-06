f = open("Calories.txt", "r")
calories = f.read()
split_calories = calories.split("\n\n")
elves = []

for x in range(len(split_calories)):
    total = 0
    split_lines = split_calories[x].splitlines()
    for y in range(len(split_lines)):
        total += int(split_lines[y])
    elves.append(total)

elves.sort(reverse=True)
total = 0

for x in range(3):
    total += int(elves[x])

print(total)
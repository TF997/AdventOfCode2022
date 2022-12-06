pairs = open("input.txt", "r").read().split("\n")
total = 0

for pair in pairs:
    bounds = pair.split(",")
    firstBounds = bounds[0].split("-")
    secondBounds = bounds[1].split("-")

    if int(firstBounds[0]) <= int(secondBounds[0]) and int(firstBounds[1]) >= int(secondBounds[1]) \
            or int(secondBounds[0]) <= int(firstBounds[0]) and int(firstBounds[1]) <= int(secondBounds[1]):
        total += 1

print(total)

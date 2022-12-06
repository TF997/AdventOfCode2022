f = open("input.txt", "r")
backpacks = f.read()
backpacks = backpacks.split("\n")
alphabet = "abcdefghijklmnopqrstuvwxyz"
total = 0
# for each backpack split the string in half
for x in range(0, len(backpacks), 3):
    # find the character that is in both first_comp and second_comp
    for char in backpacks[x]:
        if char in backpacks[x + 1] and char in backpacks[x + 2]:
            print(char)
            if char.isupper():
                print(alphabet.index(char.lower()) + 26)
                total += alphabet.index(char.lower()) + 27
            else:
                print(alphabet.index(char))
                total += alphabet.index(char) + 1
            break

print(total)

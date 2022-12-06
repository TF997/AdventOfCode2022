f = open("input.txt", "r")
backpacks = f.read()
backpacks = backpacks.split("\n")
alphabet = "abcdefghijklmnopqrstuvwxyz"
total = 0
# for each backpack split the string in half
for backpack in backpacks:
    first_comp = backpack[:len(backpack) // 2]
    second_comp = backpack[len(backpack) // 2:]

    # find the character that is in both first_comp and second_comp
    for char in first_comp:
        if char in second_comp:
            print(char)
            if char.isupper():
                print(alphabet.index(char.lower()) + 26)
                total += alphabet.index(char.lower()) + 27
            else:
                print(alphabet.index(char))
                total += alphabet.index(char) + 1
            break

print(total)

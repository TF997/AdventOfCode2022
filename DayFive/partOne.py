Instructions = open("input.txt", "r").read().split("\n")
MOVE = 1
FROM = 3
TO = 5

StackOne = ["F", "C", "J", "P", "H", "T", "W"]
StackTwo = ["G", "R", "V", "F", "Z", "J", "B", "H"]
StackThree = ["H", "P", "T", "R"]
StackFour = ["Z", "S", "N", "P", "H", "T"]
StackFive = ["N", "V", "F", "Z", "H", "J", "C", "D"]
StackSix = ["P", "M", "G", "F", "W", "D", "Z"]
StackSeven = ["M", "V", "Z", "W", "S", "J", "D", "P"]
StackEight = ["N", "D", "S"]
StackNine = ["D", "Z", "S", "F", "M"]

Stacks = [StackOne, StackTwo, StackThree, StackFour, StackFive, StackSix, StackSeven, StackEight, StackNine]

for instruction in Instructions:
    amount = int(instruction.split(" ")[MOVE])
    fromStack = int(instruction.split(" ")[FROM])
    toStack = int(instruction.split(" ")[TO])
    for x in range(amount):
        Stacks[toStack - 1].append(Stacks[fromStack - 1].pop())

for stack in Stacks:
    print(stack[-1])
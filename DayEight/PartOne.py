Trees = open("input.txt", "r").read()
# Trees into a 3d array of characters
Trees = [list(Tree) for Tree in Trees.split("\n")]

validTrees = 0
for Down in range(len(Trees)):
    for Across in range(len(Trees[Down])):
        First_valid = True
        Second_valid = True
        Third_valid = True
        Fourth_valid = True
        if Across == 0 or Down == 0 or Across == len(Trees) - 1 or Down == len(Trees[Across]) - 1:
            print("\n")
            print(Trees[Down][Across] + " is on the edge with Coordinates: " + str(Down) + ", " + str(Across))
            validTrees += 1
        else:
            print("\n")
            for i in range(Down - 1, -1, -1):
                if int(Trees[i][Across]) >= int(Trees[Down][Across]):
                    First_valid = False
                    print("First invalid: " + str(Trees[i][Across]) + " >= " + str(Trees[Down][Across]))
                    break
                else:
                    print("First valid: " + str(Trees[i][Across]) + " < " + str(Trees[Down][Across]))
            for i in range(Across - 1, -1, -1):
                if int(Trees[Down][i]) >= int(Trees[Down][Across]):
                    Second_valid = False
                    print("Second invalid: " + str(Trees[Down][i]) + " >= " + str(Trees[Down][Across]))
                    break
                else:
                    print("Second valid: " + str(Trees[Down][i]) + " < " + str(Trees[Down][Across]))
            for i in range(Across + 1, len(Trees[Down])):
                if int(Trees[Down][i]) >= int(Trees[Down][Across]):
                    Third_valid = False
                    print("Third invalid: " + str(Trees[Down][i]) + " >= " + str(Trees[Down][Across]))
                    break
                else:
                    print("Third valid: " + str(Trees[Across][i]) + " < " + str(Trees[Down][Across]))
            for i in range(Down + 1, len(Trees)):
                if int(Trees[i][Across]) >= int(Trees[Down][Across]):
                    Fourth_valid = False
                    print("Fourth invalid: " + str(Trees[i][Across]) + " >= " + str(Trees[Down][Across]))
                    break
                else:
                    print("Fourth valid: " + str(Trees[i][Across]) + " < " + str(Trees[Down][Across]))
            if First_valid or Second_valid or Third_valid or Fourth_valid:
                print(Trees[Down][Across] + " VALID with Coordinates: DOWN:" + str(Down) + ", ACROSS:" + str(Across))
                validTrees += 1
            else:
                print(Trees[Down][Across] + " INVALID with Coordinates: DOWN:" + str(Down) + ", ACROSS:" + str(Across))
print(validTrees)

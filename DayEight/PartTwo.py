Trees = open("input.txt", "r").read()
# Trees into a 3d array of characters
Trees = [list(Tree) for Tree in Trees.split("\n")]
BestScore = 0
validTrees = 0
for Down in range(len(Trees)):
    for Across in range(len(Trees[Down])):
        First_valid = True
        Second_valid = True
        Third_valid = True
        Fourth_valid = True
        First_Score = 0
        Second_Score = 0
        Third_Score = 0
        Fourth_Score = 0
        Total_Score = 0
        if Across == 0 or Down == 0 or Across == len(Trees) - 1 or Down == len(Trees[Across]) - 1:
            print("\n")
            print(Trees[Down][Across] + " is on the edge with Coordinates: " + str(Down) + ", " + str(Across))
            validTrees += 1
        else:
            print("\n")
            print(Trees[Down][Across] + " at Coordinates: " + str(Down) + ", " + str(Across))
            for i in range(Down - 1, -1, -1):
                First_Score += 1
                if int(Trees[i][Across]) >= int(Trees[Down][Across]):
                    First_valid = False
                    print("First View Blocked: " + str(Trees[i][Across]) + " >= " + str(Trees[Down][Across]))
                    break
                else:
                    print("First Score: " + str(First_Score))
            for i in range(Across - 1, -1, -1):
                Second_Score += 1
                if int(Trees[Down][i]) >= int(Trees[Down][Across]):
                    Second_valid = False
                    print("Second View Blocked: " + str(Trees[Down][i]) + " >= " + str(Trees[Down][Across]))
                    break
                else:
                    print("Second_Score: " + str(Second_Score))
            for i in range(Across + 1, len(Trees[Down])):
                Third_Score += 1
                if int(Trees[Down][i]) >= int(Trees[Down][Across]):
                    Third_valid = False
                    print("Third View Blocked: " + str(Trees[Down][i]) + " >= " + str(Trees[Down][Across]))
                    break
                else:
                    print("Third Score: " + str(Third_Score))
            for i in range(Down + 1, len(Trees)):
                Fourth_Score += 1
                if int(Trees[i][Across]) >= int(Trees[Down][Across]):
                    Fourth_valid = False
                    print("Fourth View Blocked: " + str(Trees[i][Across]) + " >= " + str(Trees[Down][Across]))
                    break
                else:
                    print("Fourth score: " + str(Fourth_Score))
            Total_Score = First_Score * Second_Score * Third_Score * Fourth_Score
            print("Total Score: " + str(Total_Score))
            if Total_Score > BestScore:
                print("New Best Score: " + str(Total_Score))
                BestScore = Total_Score
print(BestScore)

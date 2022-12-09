Instructions = open("input.txt", "r").read().split("\n")  # Read the input file


def Print_Grid():  # print the grid
    for i in range(len(Grid)):
        print(Grid[i])
    print("\n")


def Move_Right(steps, current_position, tail_position):
    starting_position = current_position[1]
    for x in range(steps):
        if x != starting_position:
            last_tail_position = tail_position
            Grid[last_tail_position[0]][last_tail_position[1]] = "#"
        tail_position = current_position
        current_position = [current_position[0], current_position[1] + 1]
        Grid[current_position[0]][current_position[1]] = "H"
        Grid[tail_position[0]][tail_position[1]] = "T"
        Print_Grid()
    return current_position, tail_position


def Move_Down(steps, current_position, tail_position):
    starting_position = current_position[0]
    for x in range(steps):
        if x != starting_position:
            last_tail_position = tail_position
            Grid[last_tail_position[0]][last_tail_position[1]] = "#"
        tail_position = current_position
        current_position = [current_position[0] + 1, current_position[1]]
        Grid[current_position[0]][current_position[1]] = "H"
        Grid[tail_position[0]][tail_position[1]] = "T"
        Print_Grid()
    return current_position, tail_position


def Move_Left(steps, current_position, tail_position):
    starting_position = current_position[1]
    for x in range(steps, 0, -1):
        # set last_tail_position to tail_position if its not the first time
        if x != starting_position:
            last_tail_position = tail_position
            Grid[last_tail_position[0]][last_tail_position[1]] = "#"
        tail_position = current_position
        current_position = [current_position[0], current_position[1] - 1]
        Grid[current_position[0]][current_position[1]] = "H"
        Grid[tail_position[0]][tail_position[1]] = "T"
        Print_Grid()
    return current_position, tail_position


def Move_Up(steps, current_position, tail_position):
    starting_position = current_position[0]
    for x in range(steps, 0, -1):
        if x != starting_position:
            last_tail_position = tail_position
            Grid[last_tail_position[0]][last_tail_position[1]] = "#"
        tail_position = current_position
        current_position = [current_position[0] - 1, current_position[1]]
        Grid[current_position[0]][current_position[1]] = "H"
        Grid[tail_position[0]][tail_position[1]] = "T"
        Print_Grid()
    return current_position, tail_position


# create a 100 x 100 grid of 0's
Grid = [["." for x in range(6)] for y in range(5)]

# set the starting point to 1
Start = [4, 0]

# set the current position to the starting point
CurrentPosition = Start
TailPosition = []
LastPosition = []
Grid[Start[0]][Start[1]] = "s"

for Instruction in Instructions:
    print(Instruction)
    LastPosition = CurrentPosition
    Direction = Instruction[0]
    Steps = Instruction[2]
    if Direction == "R":
        CurrentPosition, TailPosition = Move_Right(int(Steps), CurrentPosition, TailPosition)
    elif Direction == "D":
        CurrentPosition, TailPosition = Move_Down(int(Steps), CurrentPosition, TailPosition)
    elif Direction == "L":
        CurrentPosition, TailPosition = Move_Left(int(Steps), CurrentPosition, TailPosition)
    elif Direction == "U":
        CurrentPosition, TailPosition = Move_Up(int(Steps), CurrentPosition, TailPosition)

# remove all 'T's from the grid
for i in range(len(Grid)):
    for j in range(len(Grid[i])):
        if Grid[i][j] == "T":
            Grid[i][j] = "."

Print_Grid()
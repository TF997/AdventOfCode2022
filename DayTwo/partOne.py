f = open("input.txt", "r")
game = f.read()
rounds = game.split("\n")

def calculate_my_move(move):
    if move == "Rock":
        return 1
    if move == "Paper":
        return 2
    if move == "Scissors":
        return 3


def decrypt_move(move):
    if move == "A" or move == "X":
        return "Rock"
    if move == "B" or move == "Y":
        return "Paper"
    if move == "C" or move == "Z":
        return "Scissors"


def calculate_game_score(my_move, their_move):
    if my_move == their_move:
        return 3

    if my_move == "Rock":
        if their_move == "Paper":
            return 0
        if their_move == "Scissors":
            return 6

    if my_move == "Paper":
        if their_move == "Scissors":
            return 0
        if their_move == "Rock":
            return 6

    if my_move == "Scissors":
        if their_move == "Rock":
            return 0
        if their_move == "Paper":
            return 6


total_points = 0
for x in range(len(rounds)):
    print("Round " + str(x) + ": " + decrypt_move(rounds[x][0]) + " Vs " + decrypt_move(rounds[x][2]))
    theirMoveDecrypted = decrypt_move(rounds[x][0])
    myMoveDecrypted = decrypt_move(rounds[x][2])
    points = calculate_my_move(myMoveDecrypted)
    print("Points for move: " + str(points))
    points += calculate_game_score(myMoveDecrypted, theirMoveDecrypted)
    print("Points for game: " + str(points - calculate_my_move(myMoveDecrypted)))
    total_points += points
    print("\n")
print(total_points)

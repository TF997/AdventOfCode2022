f = open("input.txt", "r")
game = f.read()
rounds = game.split("\n")


def calculate_my_move_points(move, result):
    if move == "Rock":
        if result == 0:
            return 3  # Lose to rock play Scissors
        if result == 3:
            return 1  # Draw to rock play Rock
        if result == 6:
            return 2  # Win to rock play Paper
    if move == "Paper":
        if result == 0:
            return 1  # Lose to paper play rock
        if result == 3:
            return 2
        if result == 6:
            return 3  # Win to paper play scissors
    if move == "Scissors":
        if result == 0:
            return 2
        if result == 3:
            return 3
        if result == 6:
            return 1


def decrypt_move(move):
    if move == "A":
        return "Rock"
    if move == "B":
        return "Paper"
    if move == "C":
        return "Scissors"


def calculate_game_score(result):
    if result == "X":
        return 0
    if result == "Y":
        return 3
    if result == "Z":
        return 6


total_points = 0
for x in range(len(rounds)):
    theirMoveDecrypted = decrypt_move(rounds[x][0])
    resultDecrypted = calculate_game_score(rounds[x][2])
    points = calculate_my_move_points(theirMoveDecrypted, resultDecrypted) + resultDecrypted
    total_points += points
print(total_points)

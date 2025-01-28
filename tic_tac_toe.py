import random

gameOver = False
players = ["x","u"]
currentPlayer = random.choice(players)
game_Board = [["1","2","3"],
              ["4","5","6"],
              ["7","8","9"]]
def draw_board():
    for x in game_Board:
        print()
        for y in x:
            print(y, end="  ")
    print()
def append_to_board(position, player):
    for row in range(3):
        for col in range(3):
            if game_Board[row][col] == position:
                game_Board[row][col] = player
def alternate_players(player):
    if player == players[0]:
        player = players[1]
    elif player == players[1]:
        player = players[0]
    return player
def check_winner():
    for x in range(3):
        for y in range(3):
            if game_Board [x][0] == game_Board [x][1]== game_Board [x][2]:
                return True
            elif game_Board[0][y] == game_Board[1][y] == game_Board[2][y]:
                return True
            elif game_Board[0][0] == game_Board[1][1] == game_Board[2][2]:
                return True
            elif game_Board[0][2] == game_Board[1][1] == game_Board[2][0]:
                return True
    return False
def position_occupied(position):
    for row in game_Board:
        for item in row:
            if item == position:
                return False
    return True

def valid_input(position):
    if not position.isdigit() or int(position) <1 or int(position) >9:
        return False
    return not position_occupied(position)



print("Game of tic tac toe: use 'x' or 'u'")
print("Once a player chooses a character, player 2 -- \n"
      "--will be auto assigned to remaining character")
print("Pick a number from the board to replace with your character")

while not gameOver:
    draw_board()
    playerPos = input(f"\n{currentPlayer.upper()} turn: ")

    while not valid_input(playerPos):
        print("Invalid input. Please choose a number from 1 to 9 that hasn't been chosen.")
        playerPos = input(f"\n{currentPlayer.upper()} turn: ")

    append_to_board(playerPos, currentPlayer.upper())
    gameOver = check_winner()
    if gameOver:
        draw_board()
        print(f"Player-{currentPlayer.upper()} wins!")
        break

    currentPlayer = alternate_players(currentPlayer)
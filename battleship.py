"""
This is a simplified, one-player version of the classic board game Battleship! 
In this version of the game, there will be a single ship hidden in a random location on a 5x5 grid. 
The player will have five guesses to try to sink the ship.
"""


from random import randint

print('''
Welcome to Battleship. This is a strategy guessing game.
The computer has a single ship hidden in a random location on a 5x5 grid.
Your objective is to sink the computer"s battleship by guessing the exact location
You will get five guesses. Good luck!
''')


board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


# you can test computer's location here with print ship_row and print ship_col


# While loop to keep running the game 
while True:
    
    play_game = input('Are you ready to play? Enter Y or N.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    # Game play
    while game_on:

        # don't forget to properly indent!
        for turn in range(5):
            print("Turn", turn + 1)
            guess_row = int(input("Guess Row: "))
            guess_col = int(input("Guess Col: "))

            if guess_row == ship_row and guess_col == ship_col:
                print("Congratulations! You sank my battleship!")
                break
            else:
                if guess_row not in range(5) or guess_col not in range(5):
                    print("Oops, that's not even in the ocean.")
                elif board[guess_row][guess_col] == "X":
                    print("You guessed that one already.")
                else:
                    print("Whew! You missed my battleship!")
                    board[guess_row][guess_col] = "X"
                    
                    if (turn == 4):
                        print("Game Over")
            print_board(board)

        # this version includes a replay option
        replay = input('Do you want to play again? Enter Y or N: ')
    
        if replay.lower()[0] == 'y':
            replay = True
        else:
            print("Goodbye.")
            replay = False
            break
    # break out of the while loop on replay
    break

from random import randint

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
# uncomment the two lines to see the answer
#print ship_row
#print ship_col

# Everything from here on should be in your for loop
turn = 0
while turn <= 4:
  print("\nTurn", turn + 1)
  turn += 1
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("\nCongratulations! You sank my battleship!")
    break

  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print("\nOops, that's not even in the ocean. Try again!")
      turn -= 1
      
    elif board[guess_row][guess_col] == "X":
      print("\nYou guessed that one already.")

    else:
      print("\nYou missed my battleship!")
      board[guess_row][guess_col] = "X"
      if turn >= 4:
        print('\nGame Over')
        break
  print('\n')
  print_board(board)  

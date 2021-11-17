def battleships(board):
    row = len(board)
    col = len(board[0])

    counter = 0
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'X':
                if i == 0 and j == 0:
                    counter += 1
                elif i == 0 and j != 0:
                    if board[i][j - 1] != 'X':
                        counter += 1
                elif i != 0 and j == 0:
                    if board[i - 1][j] != 'X':
                        counter += 1
                else:
                    if board[i - 1][j] != 'X' and board[i][j - 1] != 'X':
                        counter += 1

    return counter

board = [["."]]

print(battleships(board))
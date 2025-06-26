import random

board = [[0 for _ in range(9)] for _ in range(9)]   # 9x9 Grid Of 0s

def is_valid(board, row, col, num):
    # Check Rows and Columns
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:    # Check Numbers in Row and Column
            return False
    
    #Check 3x3 Box
    l_box_row, l_box_col = 3 * (row // 3), 3 * (col // 3)   # Large Box Coords
    for i in range (3):
        for j in range(3):
            if board[l_box_row + i][l_box_col + j] == num:  # Check Numbers In Large Box
                return False
    
    return True

def fill_board(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:    # Empty Cell
                nums = list(range(1,10))
                random.shuffle(nums)

                for num in nums:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if fill_board(board):
                            return True
                        board[row][col] = 0     # Backtrack If Board Can't Be Filled
                return False
    return True

def display_board_text(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            val = board[i][j]
            print(val if val != 0 else ".", end=" ")
        print() # New Line After Each Row

fill_board(board)

display_board_text(board)
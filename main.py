import random

full_board = [[0 for _ in range(9)] for _ in range(9)]   # 9x9 Grid Of 0s
puzzle_board = [[0 for _ in range(9)] for _ in range(9)]   # 9x9 Grid Of 0s

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
    print()

def remove_numbers(board, difficulty='easy'):
    # random int [0-9] % difficulty = x (interval for removing numbers)
        # 4 % 1 = 4 -> then get new interval
        # 9 % 1 = 9

        # 2 % 5 = 0 (remove next number in grid)
        # 9 % 5 = 4 

    difficulty_levels = {
        'easy': 35,
        'medium': 45,
        'hard': 55,
        'impossible': 65
    }

    board_copy = [row[:] for row in board]
    num_to_remove = difficulty_levels.get(difficulty, 35)

    removed = 0
    while removed < num_to_remove:
        row = random.randint(0,8)
        col = random.randint(0,8)

        if board_copy[row][col] != 0:
            board_copy[row][col] = 0
            removed += 1

    return board_copy

fill_board(full_board)

print("Complete Board: ")
display_board_text(full_board)

puzzle_board = remove_numbers(full_board, 'easy')

print("Puzzle Board: ")
display_board_text(puzzle_board)
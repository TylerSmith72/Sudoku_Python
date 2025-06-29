import random
from datetime import datetime, date

full_board = [[0 for _ in range(9)] for _ in range(9)]   # 9x9 Grid Of 0s
puzzle_board = [[0 for _ in range(9)] for _ in range(9)]   # 9x9 Grid Of 0s

mistakes = 0
start_time = datetime.now()
end_time = None

print(f'Now: {start_time}\n')


def is_valid(board, row, col, num):
    global mistakes

    # Check Rows and Columns
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:    # Check Numbers in Row and Column
            mistakes += 1
            return False

    # Check 3x3 Box
    l_box_row, l_box_col = 3 * (row // 3), 3 * (col // 3)   # Large Box Coords
    for i in range(3):
        for j in range(3):
            if board[l_box_row + i][l_box_col + j] == num:  # Check Numbers In Large Box
                mistakes += 1
                return False

    return True


def reset_mistakes():
    global mistakes

    print(f'Resetting mistake counter: {mistakes} -> 0 \n')
    mistakes = 0


def fill_board(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:    # Empty Cell
                nums = list(range(1, 10))
                random.shuffle(nums)

                for num in nums:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if fill_board(board):
                            return True
                        # Backtrack If Board Can't Be Filled
                        board[row][col] = 0
                return False
    reset_mistakes()
    return True


def display_board_text(board):
    print("X | A B C | D E F | G H I")
    print("-" * 25)
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 25)

        for j in range(9):
            output = ""
            if j == 0:
                output += f'{i + 1} | '
            if j % 3 == 0 and j != 0:
                output += "| "

            val = board[i][j]

            if val == 0:
                output += "."
            else:
                output += str(val)

            print(output, end=" ")
        print()  # New Line After Each Row
    print()


def remove_numbers(board, difficulty='easy'):
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
        row = random.randint(0, 8)
        col = random.randint(0, 8)

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

# Setup Game


def setup_game():
    pass

# Start Game


def start_game():
    pass

import random
from datetime import datetime, date
from string import ascii_letters

mistakes = 0
start_time = datetime.now()
end_time = None

print(f'Now: {start_time}\n')


def is_valid(board: list[list[int]], row: int, col: int, num: int):
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


def fill_board(board: list[list[int]]) -> bool:
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


def display_board_text(board: list[list[int]], message: str):
    print(message + "\n")
    print("X | A B C | D E F | G H I")
    print("-" * 25)

    for i in range(9):      # i = Rows
        if i % 3 == 0 and i != 0:
            print("-" * 25)

        for j in range(9):  # J = Columns
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


def remove_numbers(board: list[list[int]], difficulty='easy') -> list[list]:
    difficulty_levels = {
        'easy': 2,
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


def get_user_difficulty():
    options = [
        "easy",
        "medium",
        "hard",
        "impossible",
    ]
    choice = input(
        f'Chose a difficulty | {options}: ')

    if choice not in options:
        return get_user_difficulty()

    return choice


def setup_game(full_board: list[list[int]]) -> list[list[int]]:
    fill_board(full_board)

    # display_board_text(full_board, "Complete Board: ")

    difficulty = get_user_difficulty()

    puzzle_board = remove_numbers(full_board, difficulty)

    display_board_text(puzzle_board, "Puzzle Board: ")

    return puzzle_board


def coords_to_index(coords: str) -> list:
    columns = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
    }

    letter = coords[0]
    number = coords[1]

    return [int(number) - 1, columns.get(letter)]


def get_user_coords() -> str:
    coord = input("Please enter your coordinates | E.g. (A1): ")

    if (len(coord) != 2) or (coord[0] not in ascii_letters) or (int(coord[1]) not in range(1, 10)):
        return get_user_coords()

    return coord


def get_user_number() -> int:
    number = input("Please enter your number: ")

    if int(number) not in range(1, 10):
        return get_user_number()

    return int(number)


def play_game(puzzle_board: list[list[int]], full_board: list[list[int]]) -> bool:
    while puzzle_board != full_board:
        user_coords = get_user_coords()
        user_number = get_user_number()

        board_pos = coords_to_index(user_coords)

        # Add num if valid
        if is_valid(puzzle_board, board_pos[0], board_pos[1], user_number):
            puzzle_board[board_pos[0]][board_pos[1]] = user_number

        display_board_text(puzzle_board, "")

    return True


if __name__ == "__main__":
    full_board = [[0 for _ in range(9)] for _ in range(9)]   # 9x9 Grid Of 0s

    puzzle_board = setup_game(full_board)

    if play_game(puzzle_board, full_board):
        print("You win!")

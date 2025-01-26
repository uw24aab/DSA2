import random

# chessboard size (8x8)
BOARD_SIZE = 8

# all possible knight moves in format (x, y offsets)
directions = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

# fixed starting position
START_X, START_Y = 0, 0


# function to get user input
def get_user_input():
    print("Knight's Tour Problem")
    tour_type = int(input("Enter 1 for Open Tour or 2 for Closed Tour: "))
    print("\nApproach Options:")
    approach = int(input("Enter 1 for Backtracking or 2 for Las Vegas: "))
    return tour_type, approach


# helper function to pretty display chessboard
def display_board(board):
    for row in board:
        print(" ".join(f"{cell:2}" if cell != -1 else " ." for cell in row))
    print()


# helper function to initialize chessboard
def initialize_board():
    return [[-1 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


# helper function to check if a move is valid
def is_valid_move(board, x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and board[x][y] == -1


# helper function to check if knight can move to starting position
# after completing the tour - for closed tour
def can_move_to_starting_position(current_x, current_y, start_x, start_y):
    for dx, dy in directions:
        if start_x == current_x + dx and start_y == current_y + dy:
            return True
    return False


# backtracking solution for knight Tour
def solve_backtracking(board, x, y, move_count, is_closed, start_x, start_y):
    board[x][y] = move_count

    # base case: all squares are visited
    if move_count == BOARD_SIZE * BOARD_SIZE - 1:
        # if closed tour, ensure knight can return to starting square
        if is_closed and not can_move_to_starting_position(x, y, start_x, start_y):
            # backtrack if no valid moves are left
            board[x][y] = -1
            return False
        return True

    # explore all valid moves
    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        if is_valid_move(board, next_x, next_y):
            if solve_backtracking(
                board, next_x, next_y, move_count + 1, is_closed, start_x, start_y
            ):
                return True

    # backtrack if no valid moves are left
    board[x][y] = -1
    return False


# las vegas solution for Knight tour
def solve_las_vegas(board, start_x, start_y, is_closed):
    move_count = 0
    x, y = start_x, start_y
    board[x][y] = move_count  # mark the starting position
    move_count += 1

    while move_count < BOARD_SIZE * BOARD_SIZE:
        # get all valid moves
        valid_moves = [
            (x + dx, y + dy)
            for dx, dy in directions
            if is_valid_move(board, x + dx, y + dy)
        ]

        # if no valid moves are left the attempt fails
        if not valid_moves:
            return False

        # randomly select the next move
        next_x, next_y = random.choice(valid_moves)

        # make the next move
        board[next_x][next_y] = move_count
        move_count += 1
        x, y = next_x, next_y

    # if closed tour check if knight can return to the start
    if is_closed and not can_move_to_starting_position(x, y, start_x, start_y):
        return False

    return True


# main function to run the program and get user input
def main():
    # initialize chessboard
    board = initialize_board()

    # display the initial board
    display_board(board)

    # get user input
    tour_type, approach = get_user_input()
    is_closed = tour_type == 2

    # solve the knight tour problem
    success = False
    if approach == 1:
        print("\nSolving Knight's Tour using Backtracking...")
        success = solve_backtracking(
            board, START_X, START_Y, 0, is_closed, START_X, START_Y
        )
    elif approach == 2:
        print("\nSolving Knight's Tour using Las Vegas...")
        success = solve_las_vegas(board, START_X, START_Y, is_closed)
    else:
        print("Invalid approach selected. Exiting program.")
        return

    # display the result
    if success:
        print("\nKnight's Tour completed successfully!")
        display_board(board)
    else:
        print("\nKnight's Tour failed. Here is the final board state:")
        display_board(board)


# run the program
if __name__ == "__main__":
    main()

import random as random;


def create_board(size_board):
    board = []
    for _ in range(size_board):
        row = [0] * size_board
        pos = random.randint(0, size_board - 1)
        row[pos] = 1
        board.append(row)
    return board

def create_boards (size_board, num_boards):
    boards = []
    for _ in range(num_boards):
        board = create_board(size_board)
        boards.append(board)
    return boards

def main():
    size_board = 8
    num_boards = 100
    boards = create_boards(size_board, num_boards)
    for i, board in enumerate(boards):
        print(f"Tablero {i+1}:")
        for row in board:
            print(' '.join(str(cell) for cell in row))
        print()

if __name__ == "__main__":
    main()

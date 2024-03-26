#Importa el modulo random para generar los aleatorios que se necesitaran
import random as random;

#se hace la generación de un tablero con las reinas en posiciones aleatorias
def create_board(size_board):
    board = []
    for _ in range(size_board):
        row = [0] * size_board
        pos = random.randint(0, size_board - 1)
        row[pos] = 1
        board.append(row)
    return board

#Se hace la generación de los tableros definidos, en esta caso 100 tableros, con el tamaño de 8x8
def create_boards (size_board, num_boards):
    boards = []
    for _ in range(num_boards):
        board = create_board(size_board)
        boards.append(board)
    return boards
#Se seleccionan 5 tableros aleatorios para iniciar la selección de los padres
def select_random_boards(boards):
    
    return random.sample(boards, 5)
    
def main():
    size_board = 8
    num_boards = 100
    boards = create_boards(size_board, num_boards)
    selectBoards = select_random_boards(boards)
    for i, board in enumerate(selectBoards):
        print(f"Tablero {i+1}:")
        for row in board:
            print(' '.join(str(cell) for cell in row))
        print()

if __name__ == "__main__":
    main()

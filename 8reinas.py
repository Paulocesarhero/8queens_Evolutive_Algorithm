#Importa el modulo random para generar los aleatorios que se necesitaran
import random as random;

#se hace la generación de un tablero con las reinas en posiciones aleatorias

def create_board(size_board):
    # Se crea el tablero 8 x 8 con 0 en todas las posiciones
    board = [[0]*size_board for _ in range(size_board)]
    # Se declara un set para guardar las posiciones ocupadas y que no se repitan
    occupied_positions = set()
    #Se recorre el tablero
    for _ in range(size_board):
        # Se toman posiciones aleatorias en fila y columna para colocar las reinas
        row, col = random.randint(0, size_board - 1), random.randint(0, size_board - 1)
        # Se verifica que la posición no este ocupada
        while (row, col) in occupied_positions:
            # Si la posición esta ocupada se toman nuevas posiciones
            row, col = random.randint(0, size_board - 1), random.randint(0, size_board - 1)
        # Se agrega la posición al set de posiciones ocupadas y se coloca la reina en el tablero
        occupied_positions.add((row, col))
        board[row][col] = 1

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

def calculate_fitness(selected_board):
    conflicts = 0
    # Obtiene el tamaño del tablero
    size_board = len(selected_board)
    
    # Recorre las filas
    for row in selected_board:
        #Suma las filas para obtener el numero de reinas en la fila
        num_queens = sum(row)
        #Calcula los conflictos en la fila mediante la función de aptitud de n x (n-1) / 2
        conflicts += num_queens * (num_queens - 1) // 2

    # Recorre las columnas
    for col in range(size_board):
        #Suma las columnas para obtener el numero de reinas en la columna
        num_queens = sum(selected_board[row][col] for row in range(size_board))
        #Calcula los conflictos en la columna mediante la función de aptitud de n x (n-1) / 2
        conflicts += num_queens * (num_queens - 1) // 2

    # Se identifican las diagonales
    for diff in range(-size_board + 1, size_board):
        # obtiene la diagonal que va dede la esquina superior izquierda a la inferior derecha
        diag1 = [selected_board[i][i - diff] for i in range(size_board) if 0 <= i - diff < size_board]
        # obtiene la diagonal que va dede la esquina superior derecha a la inferior izquierda
        diag2 = [selected_board[i][size_board - 1 - i - diff] for i in range(size_board) if 0 <= size_board - 1 - i - diff < size_board]
        #Suma las reinas de cada diagonal
        num_queens1 = sum(diag1)
        num_queens2 = sum(diag2)
        #Calcula los conflictos en las diagonales mediante la función de aptitud de n x (n-1) / 2
        conflicts += num_queens1 * (num_queens1 - 1) // 2
        conflicts += num_queens2 * (num_queens2 - 1) // 2

    return conflicts

def select_best_boards(boards):
    #Obtiene la aptitud de cada tablero
    fitness_boards = [(calculate_fitness(board), board) for board in boards]
    #Se combinan los tableros con su aptitud correspondiente
    boards_with_fitness = list(zip(fitness_boards, boards))
    #Se ordenan los tableros por aptitud de menor a mayor
    boards_with_fitness.sort(key=lambda x: x[0])
    # Se obtienen los padres que son los dos primeros tableros con menos choques
    parents = [board[1] for board in boards_with_fitness[:2]]  # Solo devuelve los tableros
    # Regreso los padres
    return parents

def main():
    size_board = 8
    num_boards = 100
    boards = create_boards(size_board, num_boards)
    selectBoards = select_random_boards(boards)
    bestBoards = select_best_boards(selectBoards)
    for i, board in enumerate(bestBoards):
        print(f"Tablero {i+1}:")
        for row in board:
            print(' '.join(str(cell) for cell in row))
        conflicts = calculate_fitness(board)
        print(f"Conflictos: {conflicts}")
        print()

if __name__ == "__main__":
    main()

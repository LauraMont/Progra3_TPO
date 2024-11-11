import heapq
import time
import os

# Movimientos posibles del caballo
dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

# Función para verificar si una posición está dentro del tablero
def is_safe(x, y, N):
    return 0 <= x < N and 0 <= y < N

# Heurística de Warnsdorff: contar los movimientos futuros posibles
def count_moves(x, y, visited, N):
    count = 0
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if is_safe(nx, ny, N) and not visited[nx][ny]:
            count += 1
    return count

# Branch & Bound con heurística y cálculo de nodos explorados
def knight_tour_BB(N, start_x, start_y, max_time=5):
    visited = [[False for _ in range(N)] for _ in range(N)]
    path = []
    visited[start_x][start_y] = True
    path.append((start_x, start_y))

    # Cola de prioridad para priorizar los caminos más prometedores
    queue = [(0, start_x, start_y, path, visited)]
    start_time = time.time()
    nodes_explored = 0

    while queue:
        # Verificar si el tiempo límite ha sido alcanzado
        if time.time() - start_time > max_time:
            print("Tiempo límite alcanzado. No se encontró una solución completa.")
            return None, nodes_explored

        # Extraer el siguiente nodo en función de la prioridad
        _, x, y, current_path, current_visited = heapq.heappop(queue)
        nodes_explored += 1

        # Comprobar si hemos cubierto todas las casillas
        if len(current_path) == N * N:
            return current_path, nodes_explored

        # Generar los posibles movimientos
        next_moves = []
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if is_safe(nx, ny, N) and not current_visited[nx][ny]:
                # Cálculo de cota usando movimientos futuros
                future_options = count_moves(nx, ny, current_visited, N)
                if future_options == 0 and len(current_path) < N * N - 1:
                    continue  # Podar ramas que llevan a callejones sin salida
                
                next_visited = [row[:] for row in current_visited]
                next_visited[nx][ny] = True
                next_path = current_path + [(nx, ny)]
                priority = future_options  # Usar movimientos futuros como prioridad
                next_moves.append((priority, nx, ny, next_path, next_visited))

        # Ordenar movimientos futuros por la heurística de Warnsdorff
        next_moves.sort()
        for move in next_moves:
            heapq.heappush(queue, move)

    return None, nodes_explored

# Función para mostrar el recorrido completo al final
def print_final_board(solution, N):
    if not solution:
        print("No se encontró una solución completa.")
        return
    
    board = [["__" for _ in range(N)] for _ in range(N)]
    for step, (x, y) in enumerate(solution):
        board[x][y] = f"{step+1:02}"
    print("\nRecorrido completo del caballo:")
    for row in board:
        print(" ".join(row))

# Main para ejecución con diferentes valores de N y elección de posición inicial
def main():
    try:
        N = int(input("Ingrese el tamaño del tablero (N x N): "))
        start_x = int(input(f"Ingrese la posición inicial del caballo (fila, entre 0 y {N-1}): "))
        start_y = int(input(f"Ingrese la posición inicial del caballo (columna, entre 0 y {N-1}): "))
        
        # Comprobación de límites de entrada
        if not (0 <= start_x < N and 0 <= start_y < N):
            print("La posición inicial está fuera de los límites del tablero.")
            return
        
        # Ejecutar Branch & Bound con límites de tiempo
        start_time = time.time()
        solution, nodes_explored = knight_tour_BB(N, start_x, start_y, max_time=10)
        execution_time = time.time() - start_time

        # Imprimir resultados finales
        print_final_board(solution, N)
        print(f"\nNodos explorados: {nodes_explored}")
        print(f"Tiempo de ejecución: {execution_time:.4f} segundos")

    except ValueError:
        print("Por favor, ingrese un número entero válido.")

main()

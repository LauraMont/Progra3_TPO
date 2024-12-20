import heapq
import time

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

# Algoritmo Branch & Bound 
def knight_tour_BB(N, start_x, start_y, max_time=5):
    # Paso 1: Inicialización de estructuras
    visited = [[False for _ in range(N)] for _ in range(N)]
    path = [(start_x, start_y)]
    visited[start_x][start_y] = True
    mejorSolucion = None
    start_time = time.time()
    nodes_explored = 0

    # Crear la estructura de entorno (cola de prioridad)
    env = [(0, start_x, start_y, path, visited)]  # prioridad, x, y, camino, tablero visitado

    while env:
        # Verificar si el tiempo límite ha sido alcanzado
        if time.time() - start_time > max_time:
            print("Tiempo límite alcanzado. No se encontró una solución completa.")
            return mejorSolucion, nodes_explored, time.time() - start_time

        # Paso 2: Extraer el nodo con mayor prioridad (menor número de movimientos posibles)
        _, x, y, current_path, current_visited = heapq.heappop(env)
        nodes_explored += 1

        # Paso 3: Verificar si es solución
        if len(current_path) == N * N:
            return current_path, nodes_explored, time.time() - start_time  # Solución completa encontrada

        # Paso 4: Generar hijos
        hijos = []
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if is_safe(nx, ny, N) and not current_visited[nx][ny]:
                # Cálculo de cota usando movimientos futuros
                future_options = count_moves(nx, ny, current_visited, N)
                if future_options == 0 and len(current_path) < N * N - 1:
                    continue  # Podar ramas que llevan a callejones sin salida
                
                # Crear hijo (nueva posición del caballo)
                next_visited = [row[:] for row in current_visited]
                next_visited[nx][ny] = True
                next_path = current_path + [(nx, ny)]
                
                # Paso 5: Calcular prioridad (usando movimientos futuros como heurística) y agregar a hijos
                priority = future_options
                hijos.append((priority, nx, ny, next_path, next_visited))

        # Ordenar hijos por la prioridad de Warnsdorff y agregarlos a la cola
        hijos.sort()
        for hijo in hijos:
            heapq.heappush(env, hijo)

    return mejorSolucion, nodes_explored, time.time() -start_time

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

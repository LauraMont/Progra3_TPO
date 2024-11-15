### EJERCICIO: Caballo Ajedrez
# TÉCNICA: Backtracking

#PSEUDOCÓDIGO:

# recorridoCaballo(S): -> Resuelve el recorrido del caballo. Busca un orden de movimientos que logre que se recorran todas las casillas del tablero, sin repeticiones.
# Posiciones = casillasDisponibles(S) -> Todas las posiciones no visitadas del tablero
# 	para cada p ∈ Posiciones -> Bucle que recorre todas las posiciones posibles que generamos en el paso anterior. Prueba todas las opciones una a una.
# 		avanzarPosicion(S,p) --> Va a “mover” el caballo a la nueva posición
# 		//si Factible
# 		si largo(casillasDisponibles(S))>0 || esSolucion(S) 
# 			si esSolucion(S)
# 				return S
# 			sino
# 				recorridoCaballo(S)
# 			fin si
# 		fin si
# 		volverPosicionAnterior(S,p)
# 	fin para

# avanzarPosicion: “mueve” el caballo a la nueva posición
# S: solución temporal podria ser una clase que represente los movimientos de la partida ,podría ser una matriz que represente el tablero (1: fue visitado, 0: no visitado) y un valor de ultima posicion
# Factible: hay al menos una casilla disponible con el patrón caballo o es solucion
# esSolucion: se visitaron todas las casillas , luego retorno la primera solución encontrada
# volverPosicionAnterior: caballo vuelve a la posición anterior pasada por parametro y marca posicion anterior como no visitada

import time

class TableroBT:
    def __init__(self, celdas, movimientos, x, y):
        self.N = celdas
        self.posicionInicial = (x, y)
        self.movimientosCaballo = movimientos
        self.tableroSolucion = [[-1 for _ in range(self.N)] for _ in range(self.N)]
        self.tableroSolucion[x][y] = 0  # Marca la posición inicial como visitada
        self.movimientosRealizados = 0  # Contador de movimientos

    def esMovimientoFactible(self, x, y):
        return 0 <= x < self.N and 0 <= y < self.N and self.tableroSolucion[x][y] == -1
    
    def recorridoCaballo(self):
        # Inicia el contador de tiempo
        inicio = time.time()
        
        # Ejecuta el recorrido
        solucion = self.recorridoCaballo_recursivo(self.posicionInicial, 1)
        
        # Calcula el tiempo transcurrido
        fin = time.time()
        self.tiempoTotal = fin - inicio
        
        return solucion
    
    def recorridoCaballo_recursivo(self, posicion, mov_i):
        if mov_i == self.N * self.N:
            return True

        x, y = posicion
        for dx, dy in self.movimientosCaballo:
            nx, ny = x + dx, y + dy
            if self.esMovimientoFactible(nx, ny):
                self.tableroSolucion[nx][ny] = mov_i
                self.movimientosRealizados += 1  # Cuenta el movimiento
                if self.recorridoCaballo_recursivo((nx, ny), mov_i + 1):
                    return True
                self.tableroSolucion[nx][ny] = -1  # Backtracking
        return False

    def imprimirTablero(self):
        if any(-1 in row for row in self.tableroSolucion):
            print("No se encontró solución.")
            return

        separador = "+----" * self.N + "+"
        for row in self.tableroSolucion:
            print(separador)
            print("".join(f"| {val:02} " for val in row) + "|")
        print(separador)

        # Imprime estadísticas de ejecución
        print(f"\nMovimientos realizados: {self.movimientosRealizados}")
        print(f"Tiempo total: {self.tiempoTotal:.4f} segundos")


# PRUEBA
if __name__ == "__main__":
    # Solicitar tamaño del tablero y la posición inicial del caballo
    N = int(input("Ingrese el tamaño del tablero (N): "))
    x_inicio = int(input(f"Ingrese la fila de la posición inicial del caballo (0 a {N-1}): "))
    y_inicio = int(input(f"Ingrese la columna de la posición inicial del caballo (0 a {N-1}): "))

    # Validar que la posición esté dentro de los límites del tablero
    if not (0 <= x_inicio < N and 0 <= y_inicio < N):
        print("La posición inicial es inválida. Debe estar dentro de los límites del tablero.")
    else:
        movimientos = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        tablero = TableroBT(N, movimientos, x_inicio, y_inicio)

        if tablero.recorridoCaballo():
            tablero.imprimirTablero()
        else:
            print("No se encontró solución.")

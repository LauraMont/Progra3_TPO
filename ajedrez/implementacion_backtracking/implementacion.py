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


class Tablero:
    #Definimos el tamaño del tablero
    def __init__(self, celdas, movimientos, x, y):
        self.N = celdas
        # Establecemos las coordenadas de la posicion inicial (X,Y)
        self.posicionInicial = (x-1, y-1) # Para que 1,1 sea en la coordinada inicial cuando construimos
        # Los posibles movimientos del caballo
        self.movimientosCaballo = movimientos
        # Tablero con las soluciones
        self.tableroSolucion = [[-1 for _ in range(self.N)] for _ in range(self.N)]
        # Para flaguear si se encontró la solución
        self.solucionado = False
        #Iniciar tablero con los valores que determinamos  
        self.iniciarTablero()

    
    # Funcion para determinar si el movimiento es factible o no, las condiciones son:
    # 1. Se encuentra dentro de los rangos del tablero
    # 2. Que la casilla no haya sido visitada (casilla == -1) 
    def esMovimientoFactible(self, posicion, tablero):
        x, y = posicion
        return 0 <= x < self.N and 0 <= y < self.N and tablero[x][y] == -1
    
    # Inicializamos el tablero con todas las celdas en -1 (no visitadas)
    def iniciarTablero(self):
        for i in range(self.N):
            for j in range(self.N):
                self.tableroSolucion[i][j] = -1
        # Punto de partida
        x, y = self.posicionInicial
        self.tableroSolucion[x][y] = 0

    def recorridoCaballo(self):
        self.iniciarTablero()
        self.solucionado = self.recorridoCaballo_recursivo(self.posicionInicial, 1, self.tableroSolucion)
        return self.solucionado
    
    # Función recursiva que vamos a usar para encontrar la solución
    def recorridoCaballo_recursivo(self, posicion, mov_i, tableroSolucion):

        # Log: muestra el movimiento actual y la posición
        print(f"Intentando movimiento {mov_i} en posición {posicion}")
        if mov_i == self.N * self.N:
            return True

        for movimiento in self.movimientosCaballo:
            posicionSiguiente = (posicion[0] + movimiento[0], posicion[1] + movimiento[1])
            if self.esMovimientoFactible(posicionSiguiente, tableroSolucion):
                tableroSolucion[posicionSiguiente[0]][posicionSiguiente[1]] = mov_i
                print(f"Se movio a {posicionSiguiente} (movimiento {mov_i})")
                if self.recorridoCaballo_recursivo(posicionSiguiente, mov_i + 1, tableroSolucion):
                    return True
                else:
                    # Backtracking
                    tableroSolucion[posicionSiguiente[0]][posicionSiguiente[1]] = -1
                    print(f"Backtracking desde {posicionSiguiente} (movimiento {mov_i})")
        return False

     # Obtener el recorrido de la solución
    def obtenerRecorridoSolucion(self, tableroSolucion):
        recorridoSolucion = [None] * (self.N * self.N)
        for movimiento in range(self.N * self.N):
            encontrado = False
            for y in range(self.N):
                for x in range(self.N):
                    if tableroSolucion[x][y] == movimiento:
                        recorridoSolucion[movimiento] = (y, x)
                        encontrado = True
                        break
                if encontrado:
                    break
        return recorridoSolucion

    # Imprimir el tablero de solución y el recorrido realizado
    def imprimirTablero(self):
        if not self.solucionado:
            return

        separador = "+----" * self.N + "+"

        for x in range(self.N):
            print(separador)
            for y in range(self.N):
                print(f"| {self.tableroSolucion[x][y]:02} ", end="")
            print("|")
        print(separador)

        print("\nRecorrido realizado:\n")
        movimiento = 0
        for posicion in self.obtenerRecorridoSolucion(self.tableroSolucion):
            if movimiento >= self.N:
                print()
                movimiento = 0
            print(f"({posicion[1] + 1}, {posicion[0] + 1})  ", end="")
            movimiento += 1
        print()


# PRUEBA EN EJECUCION SOLO POR CONSOLA:
if __name__ == "__main__":
    # Solicitar al usuario el tamaño del tablero y la posición inicial
    N = int(input("Ingrese el tamaño del tablero (N): "))
    x_inicio = int(input("Ingrese la posición inicial FILA del caballo: "))
    y_inicio = int(input("Ingrese la posición inicial COLUMNA del caballo: "))

    movimientos = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    tablero = Tablero(N, movimientos, x_inicio, y_inicio)

    if tablero.recorridoCaballo():
        tablero.imprimirTablero()
    else:
        print("No se encontró solución.")
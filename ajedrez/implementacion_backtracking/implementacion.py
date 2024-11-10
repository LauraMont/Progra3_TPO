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

#Casilla -1 -> No ha sido visitada

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
    
    
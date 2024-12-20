import pygame
import sys
from implementacion import TableroBT

def renderizar_tablero(screen, tablero, N, tiempo_total, nodos_recorridos):
    # Renderizar el tablero de ajedrez
    for x in range(N):
        for y in range(N):
            rect = pygame.Rect(y * 60, x * 60, 60, 60)
            color = (255, 255, 255) if (x + y) % 2 == 0 else (0, 0, 0)
            pygame.draw.rect(screen, color, rect)
            if tablero[x][y] != -1:  # Si hay un número en la casilla, mostrarlo
                font = pygame.font.Font(None, 36)
                text = font.render(str(tablero[x][y]), True, (255, 0, 0))
                screen.blit(text, (y * 60 + 20, x * 60 + 20))
    # Renderizar el tiempo total de ejecución y nodos recorridos
    font = pygame.font.Font(None, 26)
    tiempo_text = font.render(f"Tiempo de ejecucion: {tiempo_total:.2f} s", True, (255, 255, 255))
    nodos_text = font.render(f"Nodos recorridos: {nodos_recorridos}", True, (255, 255, 255))
    screen.blit(tiempo_text, (10, N * 60 + 10))
    screen.blit(nodos_text, (10, N * 60 + 40))
    pygame.display.flip()


def mostrar_mensaje(screen, mensaje):
    font = pygame.font.Font(None, 36)
    text = font.render(mensaje, True, (255, 0, 0))
    screen.blit(text, (100, 100))
    pygame.display.flip()


def main():
    pygame.init()

    # Solicitar al usuario el tamaño del tablero y la posición inicial
    N = int(input("Ingrese el tamaño del tablero (N): "))
    x_inicio = int(input("Ingrese la posición inicial FILA del caballo: "))
    y_inicio = int(input("Ingrese la posición inicial COLUMNA del caballo: "))

    # Posibles movimientos del caballo
    movimientos = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    tablero = TableroBT(N, movimientos, x_inicio, y_inicio)

    # Si no hay solución, mostrar el mensaje y salir
    if not tablero.recorridoCaballo():
        print("No hay solucion para ese tablero.")
        return

    # Si hay solución, iniciar pygame y la pantalla
    screen = pygame.display.set_mode((N * 60, N * 60 + 100))
    pygame.display.set_caption('Recorrido del Caballo')

    renderizar_tablero(screen, tablero.tableroSolucion, N, tablero.tiempoTotal, tablero.nodosRecorridos)

    # Mantener la pantalla abierta hasta que el usuario cierre la ventana
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
import pygame
import sys
import time
from implementacion import knight_tour_BB  # Importamos la función de Branch & Bound

def renderizar_tablero(screen, path, N, nodes_explored, total_time):
    """Renderizar el tablero y el recorrido paso a paso."""
    # Crear el tablero
    for x in range(N):
        for y in range(N):
            rect = pygame.Rect(y * 60, x * 60, 60, 60)
            color = (255, 255, 255) if (x + y) % 2 == 0 else (0, 0, 0)
            pygame.draw.rect(screen, color, rect)

    # Dibujar el recorrido del caballo paso a paso
    for step, (x, y) in enumerate(path):
        pygame.draw.circle(screen, (255, 0, 0), (y * 60 + 30, x * 60 + 30), 20)
        font = pygame.font.Font(None, 36)
        text = font.render(str(step + 1), True, (255, 255, 255))
        screen.blit(text, (y * 60 + 20, x * 60 + 20))

    # Mostrar los nodos recorridos y el tiempo de ejecución
    font = pygame.font.Font(None, 26)
    nodes_text = font.render(f'Nodos explorados: {nodes_explored}', True, (255, 255, 255))
    screen.blit(nodes_text, (10, N * 60 + 10))  # Asegurándonos de que esté dentro de la ventana visible
    
    time_text = font.render(f'Tiempo total: {total_time:.2f} s', True, (255, 255, 255))
    screen.blit(time_text, (10, N * 60 + 50))  # Ajusta la posición si es necesario

    pygame.display.flip()  # Llamar a flip() después de dibujar todo

def main():
    pygame.init()

    # Solicitar tamaño del tablero y posición inicial
    N = int(input("Ingrese el tamaño del tablero (N): "))
    x_inicio = int(input("Ingrese la posición inicial FILA del caballo: "))
    y_inicio = int(input("Ingrese la posición inicial COLUMNA del caballo: "))

    # Llamar al algoritmo Branch & Bound
    path, nodes_explored, total_time = knight_tour_BB(N, x_inicio, y_inicio, max_time=500)

    if path is None:
        print("No se encontró solución.")
        return

    # Iniciar pygame y la pantalla
    screen = pygame.display.set_mode((N * 60, N * 60 + 100))  # Asegúrate de que haya suficiente espacio para los textos
    pygame.display.set_caption('Recorrido del Caballo - Branch & Bound')

    renderizar_tablero(screen, path, N, nodes_explored, total_time)

    # Mantener la pantalla abierta hasta que el usuario cierre la ventana
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()

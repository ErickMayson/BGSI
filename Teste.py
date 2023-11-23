import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela
width, height = 800, 600
window_size = (width, height)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Quadrado em Pygame")

# Configurações do quadrado
square_size = 50
background_color = (169, 169, 169)  # Cinza
square_color = (99, 13, 7)  # RGB(99, 13, 7) para o quadrado
square_position = [width // 2 - square_size // 2, height // 2 - square_size // 2]

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Desenha o fundo cinza
    screen.fill(background_color)

    # Desenha o quadrado na cor RGB(99, 13, 7)
    pygame.draw.rect(screen, square_color, (square_position[0], square_position[1], square_size, square_size))

    # Atualiza a tela
    pygame.display.flip()

    # Define a taxa de atualização
    pygame.time.Clock().tick(60)

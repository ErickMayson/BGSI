# Example file showing a circle moving on screen
import pygame
from circle import Circle
from Janelas.janelaControladorDeCor import janelaControladorCor


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# create a Circle object
player = Circle(10)
janela = janelaControladorCor()
#janela.mudarCor = 
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    janela.spawn()
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # draw the Circle object on the screen
    player.move()
    player.draw(screen)

    

    # flip() the display to put your work on screen
    # pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
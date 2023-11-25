import pygame


class Circle:
    def __init__(self, radius):
        self.color = (255, 255, 255)
        self.radius = radius
        self.x = 1280/2
        self.y = 720/2
        self.speed = 100  # pixels per second
        self.last_update = pygame.time.get_ticks()

    def area(self):
        return 3.14 * (self.radius ** 2)

    def circumference(self):
        return 2 * 3.14 * self.radius

    def move(self):
        now = pygame.time.get_ticks()
        dt = now - self.last_update
        self.last_update = now
        self.x += self.speed * dt / 1000.0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        pygame.display.flip()

    def setColor(self, color = (255, 255, 255)):
        self.color = color

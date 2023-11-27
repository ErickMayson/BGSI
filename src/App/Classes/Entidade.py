import pygame
from operator import add

class Entidade:
    def __init__(self, nome, escala, translacao = (0,0), corBorda = (0,0,0), corPreenchimento = (255, 255, 255)):
        self.corBorda = corBorda
        self.corPreenchimento = corPreenchimento
        self.nome = nome
        self.escala = escala
        self.translacao = translacao

class Retangulo(Entidade):
    def __init__(self, cordsMin, cordsMax, nome, escala, translacao = (0,0), corBorda = (0,0,0), corPreenchimento = (255, 255, 255) ):
        super().__init__(nome, escala, translacao, corBorda = (0,0,0), corPreenchimento = (255, 255, 255))
        self.cordsMin = list(map(lambda x: x * escala, map(add, cordsMin, translacao)))
        self.cordsMax = list(map(lambda x: x * escala, map(add, cordsMax, translacao)))

    
    def draw(self, surf):
        pygame.draw.rect(surf, self.corPreenchimento, (self.cordsMin, self.cordsMax))
        pygame.display.flip()

class Linha(Entidade):
    def __init__(self, cordsMin, cordsMax, nome, escala, translacao = (0,0), corBorda = (0,0,0), corPreenchimento = (255, 255, 255) ):
        print("Construtor da classe Linha");
        super().__init__(nome, escala, posicao, corBorda = (0,0,0), corPreenchimento = (255, 255, 255))
        self.cordsMin = list(map(lambda x: x * escala, map(add, cordsMin, translacao)))
        self.cordsMax = list(map(lambda x: x * escala, map(add, cordsMax, translacao)))
    
    def draw(self, surf):
        pygame.draw.line(surf, self.corPreenchimento, self.cordsMin, self.cordsMax)
        pygame.display.flip()

import pygame
from operator import add
import sys
import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

class Entidade:
    def __init__(self, nome, escala, rotacao, translacao, corBorda = (0,0,0), corPreenchimento = (255, 255, 255)):
        self.corBorda = corBorda
        self.corPreenchimento = corPreenchimento
        self.nome = nome
        self.escala = escala
        self.translacao = translacao
        self.rotacao = rotacao

        

class Retangulo(Entidade):
    def __init__(self, cordsMin, cordsMax, nome, escala, rotacao, translacao, corBorda = (0,0,0), corPreenchimento = (255, 255, 255) ):
        super().__init__(nome, escala, rotacao, translacao, corBorda = (0,0,0), corPreenchimento = (255, 255, 255))
        self.cordsMin = cordsMin
        self.cordsMax = cordsMax

    
    def draw(self, surf):
        
        self.cordsMax = list(map(add, self.cordsMax, self.translacao))
        self.cordsMin = list(map(add, self.cordsMin, self.translacao))
        
        surf.fill("black")
        pygame.draw.rect(surf, self.corPreenchimento, (self.cordsMin, self.cordsMax))
        pygame.display.flip()

class Linha(Entidade):
    def __init__(self, cordsMin, cordsMax, nome, escala, rotacao = 0, translacao = (0,0), corBorda = (0,0,0), corPreenchimento = (255, 255, 255) ):
        print("Construtor da classe Linha");
        super().__init__(nome, escala, rotacao, translacao, corBorda = (0,0,0), corPreenchimento = (255, 255, 255))
        self.cordsMin = cordsMin
        self.cordsMax = cordsMax
    
    def draw(self, surf):
        self.cordsMax = list(map(add, self.cordsMax, self.translacao))
        self.cordsMin = list(map(add, self.cordsMin, self.translacao))
        
        surf.fill("black")
        pygame.draw.line(surf, self.corPreenchimento, self.cordsMin, self.cordsMax)
        pygame.display.flip()

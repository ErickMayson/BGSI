import pygame
from operator import add
import sys
import os
from .utils import *
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

class Entidade:
    def __init__(self, nome, escala = (1, 1), rotacao = 0, translacao = (0, 0), corBorda = (0,0,0), corPreenchimento = (255, 255, 255)):
        self.corBorda = corBorda
        self.corPreenchimento = corPreenchimento
        self.nome = nome
        self.escala = escala
        self.translacao = translacao
        self.rotacao = rotacao
        
    def to_dict(self):
        return {
            'tipo': 'Entidade',
            'nome': self.nome,
            'escala': self.escala,
            'rotacao': self.rotacao,
            'translacao': self.translacao,
            'corBorda': self.corBorda,
            'corPreenchimento': self.corPreenchimento
    }

        

class Retangulo(Entidade):
    def __init__(self, cordsMin, tamanho, nome, escala = (1, 1), rotacao = 0, translacao = (0, 0), corBorda = (0,0,0), corPreenchimento = (255, 255, 255) ):
        super().__init__(nome, escala, rotacao, translacao, corBorda = (0,0,0), corPreenchimento = (255, 255, 255))
        self.cordsMin = cordsMin
        self.tamanho = tamanho
        
    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            'tipo': self.__class__.__name__, 
            'cordsMin': self.cordsMin,
            'tamanho': self.tamanho
        })
        return base_dict
    
    def draw(self, surf):
        #Cords max é na verdade o tamanho do retângulo.
        #self.cordsMax = list(map(add, self.cordsMax, self.translacao))
        self.cordsMin = list(map(add, self.cordsMin, self.translacao))
        
        #print("Escala: ", self.escala, " cordsMin: ", self.cordsMin, " tamanho: ", self.tamanho)

        self.cordsMin, self.tamanho = scaleEntityRet(self.tamanho, self.cordsMin, self.escala)
        
        #print("cordsMin: ", self.cordsMin, " tamanho: ", self.tamanho)

        pygame.draw.rect(surf, self.corPreenchimento, (self.cordsMin, self.tamanho))
        pygame.display.flip()

class Linha(Entidade):
    def __init__(self, cordsMin, cordsMax, nome, escala = (1, 1), rotacao = 0, translacao = (0, 0), corBorda = (0,0,0), corPreenchimento = (255, 255, 255) ):
        #print("Construtor da classe Linha");
        super().__init__(nome, escala, rotacao, translacao, corBorda = (0,0,0), corPreenchimento = (255, 255, 255))
        self.cordsMin = cordsMin
        self.cordsMax = cordsMax
        
    def to_dict(self):
        return {
            'tipo': 'Linha',
            'cordsMin': self.cordsMin,
            'cordsMax': self.cordsMax,
            **super().to_dict()
        }
    
    def draw(self, surf):
        #print("Draw da classe Linha");
        self.cordsMax = list(map(add, self.cordsMax, self.translacao))
        self.cordsMin = list(map(add, self.cordsMin, self.translacao))
        
        newCords = scaleEntity([self.cordsMin, self.cordsMax], self.escala)
        self.cordsMin = newCords[0]
        self.cordsMax = newCords[1]

        #print("cordsMin: ", self.cordsMin, " cordsMax: ", self.cordsMax)

        pygame.draw.line(surf, self.corPreenchimento, self.cordsMin, self.cordsMax)
        pygame.display.flip()

class Poligono(Entidade):
    def __init__(self, coords, nome, escala = (1, 1), rotacao = 0, translacao = (0, 0), corBorda = (0,0,0), corPreenchimento = (255, 255, 255)):
        super().__init__(nome, escala, rotacao, translacao, corBorda, corPreenchimento)
        self.coords = coords
        
    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            'tipo': self.__class__.__name__,
            'coords': self.coords
        })
        return base_dict

    def draw(self, surf):
        #print("Draw da classe Triangulo");
        #for coord in self.coords:
        #    coord = list(map(add, coord, self.translacao))

        for i in range(len(self.coords)):
            self.coords[i] = list(map(add, self.coords[i], self.translacao))
        
        newCords = scaleEntity(self.coords, self.escala)
        for i in range(len(self.coords)):
            self.coords[i] = newCords[i]


        pygame.draw.polygon(surf, self.corPreenchimento, self.coords)
        pygame.display.flip()

class Circulo(Entidade):
    def __init__(self, cordsCenter, radius, nome, escala = (1, 1), rotacao = 0, translacao = (0, 0), corBorda = (0,0,0), corPreenchimento = (255, 255, 255)):
        super().__init__(nome, escala, rotacao, translacao, corBorda, corPreenchimento)
        self.cordsCenter = cordsCenter
        self.radius = radius
        
    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            'tipo': self.__class__.__name__,
            'cordsCenter': self.cordsCenter,
            'radius': self.radius
        })
        return base_dict

    def draw(self, surf):
        #print("Draw da classe Circle");
        self.cordsCenter = list(map(add, self.cordsCenter, self.translacao))
        

        pygame.draw.circle(surf, self.corPreenchimento, self.cordsCenter, self.radius*self.escala[0])
        pygame.display.flip()
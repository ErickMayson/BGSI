import pygame
from .Entidade import Entidade

#Singleton?
class GerenciadorObjetos:
    def __init__(self, surface):
        self.entidadesCriadas = []
        self.surface = surface

    def addEntidade(self, entidade):
        self.entidadesCriadas.append(entidade)

    def draw(self):
        for entidade in self.entidadesCriadas:
            entidade.draw(self.surface)

    
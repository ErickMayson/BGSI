import pygame
from .Entidade import Entidade

#Singleton?
class GerenciadorObjetos:
    def __init__(self, surface):
        self.entidadesCriadas = []
        self.surface = surface

    def addEntidade(self, entidade):
        if self.findEntidadeByName(entidade.nome) == None:
            self.entidadesCriadas.append(entidade)
        else:
            raise Exception("Já existe uma entidade com esse nome!")

    def draw(self):
        for entidade in self.entidadesCriadas:
            entidade.draw(self.surface)

    def findEntidadeByName(self, nome):
        for entidade in self.entidadesCriadas:
            if entidade.nome == nome:
                return entidade
        else:
            return None

    
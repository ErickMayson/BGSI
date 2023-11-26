import pygame

class Entidade:
    def __init__(self, nome, escala, posicao, corBorda = (0,0,0), corPreenchimento = (255, 255, 255)):
        self.corBorda = corBorda
        self.corPreenchimento = corPreenchimento
        self.nome = nome
        self.escala = escala
        self.posicao = posicao

class Retangulo(Entidade):
    def __init__(self, cordsMin, cordsMax, nome, escala, posicao, corBorda = (0,0,0), corPreenchimento = (255, 255, 255) ):
        super().__init__(nome, escala, posicao, corBorda = (0,0,0), corPreenchimento = (255, 255, 255))
        self.cordsMin = cordsMin
        self.cordsMax = cordsMax
    
    def draw(self, surf):
        pygame.draw.rect(surf, self.corPreenchimento, (self.cordsMin, self.cordsMax))
        pygame.display.flip()

class Linha(Entidade):
    def __init__(self, cordsMin, cordsMax, nome, escala, posicao, corBorda = (0,0,0), corPreenchimento = (255, 255, 255) ):
        print("Construtor da classe Linha");
        super().__init__(nome, escala, posicao, corBorda = (0,0,0), corPreenchimento = (255, 255, 255))
        self.cordsMin = cordsMin
        self.cordsMax = cordsMax
    
    def draw(self, surf):
        pygame.draw.line(surf, self.corPreenchimento, self.cordsMin, self.cordsMax)
        pygame.display.flip()

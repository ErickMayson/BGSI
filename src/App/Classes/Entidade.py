import pygame
from operator import add


# #funcao para rotacionar o retângulo
#         def rotacionarRet(tela, cor, x, y, largura, altura, angulo):
#             ret_rotate = pygame.Surface((largura, altura), pygame.SRCALPHA)
#             ret_rotate.fill((0, 0, 0, 0))
#             pygame.draw.rect(ret_rotate, cor, (0, 0, largura, altura))

#             rotacao = pygame.transform.rotate(ret_rotate, angulo)
#             novo_retangulo = rotacao.get_rect(center = (x, y))
#             tela.blit(rotacao, novo_retangulo.topleft)


class Entidade:
    def __init__(self, nome, escala, rotacao = 0 ,translacao = (0,0), corBorda = (0,0,0), corPreenchimento = (255, 255, 255)):
        self.corBorda = corBorda
        self.corPreenchimento = corPreenchimento
        self.nome = nome
        self.escala = escala
        self.translacao = translacao
        self.rotacao = rotacao

        

class Retangulo(Entidade):
    def __init__(self, cordsMin, cordsMax, nome, escala, rotacao = 0, translacao = (0,0), corBorda = (0,0,0), corPreenchimento = (255, 255, 255) ):
        super().__init__(nome, escala, translacao, corBorda = (0,0,0), corPreenchimento = (255, 255, 255))
        self.cordsMin = list(map(lambda x: x * escala, map(add, cordsMin, translacao)))
        self.cordsMax = list(map(lambda x: x * escala, map(add, cordsMax, translacao)))

    
    def draw(self, surf):
        pygame.draw.rect(surf, self.corPreenchimento, (self.cordsMin, self.cordsMax))
        pygame.display.flip()

class Linha(Entidade):
    def __init__(self, cordsMin, cordsMax, nome, escala, rotacao = 0, translacao = (0,0), corBorda = (0,0,0), corPreenchimento = (255, 255, 255) ):
        print("Construtor da classe Linha");
        super().__init__(nome, escala, posicao, corBorda = (0,0,0), corPreenchimento = (255, 255, 255))
        self.cordsMin = list(map(lambda x: x * escala, map(add, cordsMin, translacao)))
        self.cordsMax = list(map(lambda x: x * escala, map(add, cordsMax, translacao)))
    
    def draw(self, surf):
        pygame.draw.line(surf, self.corPreenchimento, self.cordsMin, self.cordsMax)
        pygame.display.flip()

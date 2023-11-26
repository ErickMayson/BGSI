# Importa toda a biblioteca do tk para o programa.   
from tkinter import *
# Importa o submódulo ttk para o programa, contem funcionalidades mais atualizadas.
from tkinter import ttk

import pygame

pygameWindow = {'size': (800, 400), 'backgroundColor': (255, 255, 255), 'caption': 'Janela PyGame'}
janelaPygame = pygame.display.set_mode(pygameWindow['size'])
pygame.display.set_caption(pygameWindow['caption'])


entidadesCriadas = []

from entidades.Entidade import Retangulo

retangulo1 = Retangulo((50, 50), (120, 200), 'retangulo1', 1, 1)
entidadesCriadas.append(retangulo1)
retangulo2 = Retangulo((100, 110), (154, 300), 'retangulo2', 1, 1)
entidadesCriadas.append(retangulo2)

from janelas.jGerenciadorObjetos import jGerenciadorObjetos
from janelas.jPrincipal import jPrincipal

#jGerenciadorObjetos()
#print("Barata")
#executar()
#jGerenciadorObjetos()

jPrincipal()


# running = True
# while running:
#     for event in pygame.event.get():
#         if (event.type == pygame.QUIT):
#             running = False
#     for entidade in entidadesCriadas:
#         entidade.draw(janelaPygame)
#     #jGerenciadorObjetos()

pygame.quit()
quit()
import subprocess
import sys
import os
import pygame
from Classes.GerenciadorObjetos import GerenciadorObjetos
from Classes.Entidade import Retangulo, Linha, Poligono, Circulo

def app():
    script_path = os.path.join(os.path.dirname(__file__), "Windows/Interface.py")
    subprocess.run([sys.executable, script_path], check=True)

if __name__ == "__main__":

    pygameWindow = {'size': (800, 800), 'backgroundColor': (255, 255, 255), 'caption': 'Janela PyGame'}
    janelaPygame = pygame.display.set_mode(pygameWindow['size'])
    pygame.display.set_caption(pygameWindow['caption'])

    gerenciadorSINGLETON = GerenciadorObjetos(janelaPygame)
    try:
        gerenciadorSINGLETON.loadDisplayFile('displayFile.json')
    except Exception as e:
    #Nao precisava do pass aqui, viajei
        print(e)
    

    gerenciadorSINGLETON.draw()

    from Windows.Interface import main
    main(gerenciadorSINGLETON)
    
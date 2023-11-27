import subprocess
import sys
import os
import pygame
from Classes.GerenciadorObjetos import GerenciadorObjetos
from Classes.Entidade import Retangulo
print(sys.path)

def app():
    script_path = os.path.join(os.path.dirname(__file__), "Windows/Interface.py")
    subprocess.run([sys.executable, script_path], check=True)

if __name__ == "__main__":

    pygameWindow = {'size': (800, 400), 'backgroundColor': (255, 255, 255), 'caption': 'Janela PyGame'}
    janelaPygame = pygame.display.set_mode(pygameWindow['size'])
    pygame.display.set_caption(pygameWindow['caption'])

    gerenciadorSINGLETON = GerenciadorObjetos(janelaPygame)

    retangulo1 = Retangulo((50, 50), (120, 200), 'retangulo1', 3, (45,45))
    GerenciadorObjetos.addEntidade(gerenciadorSINGLETON, retangulo1)
    #retangulo2 = Retangulo((100, 110), (154, 300), 'retangulo2', 1, 1)
    #gerenciadorSINGLETON.addEntidade(retangulo2)

    gerenciadorSINGLETON.draw()

    from Windows.Interface import main
    #print(sys.path)
    main(gerenciadorSINGLETON)
    
    
    
    #app()
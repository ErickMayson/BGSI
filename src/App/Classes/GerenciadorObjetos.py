import pygame
from .Entidade import Entidade, Retangulo, Linha
import json

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
        self.surface.fill("black")
        for entidade in self.entidadesCriadas:
            entidade.draw(self.surface)

    def findEntidadeByName(self, nome):
        if type(nome) != str:
            str(nome)
        for entidade in self.entidadesCriadas:
            if entidade.nome == nome:
                return entidade
        else:
            return None
        
    def to_dict(self):
        return {
            'entidadesCriadas': [entidade.to_dict() for entidade in self.entidadesCriadas],
            'surface_size': (self.surface.get_width(), self.surface.get_height())
               }
    
    def saveDisplayFile(self):
        with open("displayFile.json", 'w') as displayFile:
            json.dump(self.to_dict(), displayFile, indent=2)
            
    def loadDisplayFile(self, filename):
        with open(filename, 'r') as displayFile:
            data = json.load(displayFile)
            self.entidadesCriadas = [self.loadEntidades(entidade_data) for entidade_data in data.get('entidadesCriadas', [])]

    def loadEntidades(self, entidade_data):
        tipo = entidade_data.get('tipo', 'Entidade')

        if tipo == 'Entidade':
            return Entidade(nome=entidade_data['nome'],
                             escala=entidade_data['escala'],
                             rotacao=entidade_data['rotacao'],
                             translacao=entidade_data['translacao'],
                             corBorda=entidade_data['corBorda'],
                             corPreenchimento=entidade_data['corPreenchimento'])
        elif tipo == 'Retangulo':
            return Retangulo(cordsMin=entidade_data['cordsMin'],
                             tamanho=entidade_data['tamanho'],
                             nome=entidade_data['nome'],
                             escala=entidade_data['escala'],
                             rotacao=entidade_data['rotacao'],
                             translacao=entidade_data['translacao'],
                             corBorda=entidade_data['corBorda'],
                             corPreenchimento=entidade_data['corPreenchimento'])
        elif tipo == 'Linha':
            return Linha(cordsMin=entidade_data['cordsMin'],
                         cordsMax=entidade_data['cordsMax'],
                         nome=entidade_data['nome'],
                         escala=entidade_data['escala'],
                         rotacao=entidade_data['rotacao'],
                         translacao=entidade_data['translacao'],
                         corBorda=entidade_data['corBorda'],
                         corPreenchimento=entidade_data['corPreenchimento'])
        else:
            # Handle other types if needed
            return None
import pygame


#Não consigo fazer isso aqui funcionar 😭😭😭(Com o Tkinter no caso)
#Se possível, passar os nomes para CamelCase, comecei fazer com _ pra dar uma variada e achei uma porcaria

class CreateObject:
    def __init__(self, object_name, object_type, coordinates):
        self.object_name = object_name
        self.object_type = object_type
        self.coordinates = coordinates

class ObjectManager:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def draw_objects(self, screen):
        for obj in self.objects:
            if obj.object_type == "Reta":
                pygame.draw.line(screen, (255, 0, 0), (obj.coordinates[0], obj.coordinates[1]), (obj.coordinates[2], obj.coordinates[3]), 2)
            elif obj.object_type == "Quadraticos":
                # Placeholder
                pass
            elif obj.object_type == "Triangulo":
                # Placeholder
                pass
            elif obj.object_type == "Circulo":
                # Placeholder
                pass

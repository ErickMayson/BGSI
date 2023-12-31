import math

def scaleEntity(vertices = [[0,0]], scale = (1, 1)):
    # Move os vertices para a origem
    center = getCenter(vertices)
    for i in range(len(vertices)):
        vertices[i] = [vertices[i][0] - center[0], vertices[i][1] - center[1]]

    # Escala os vertices
    for i in range(len(vertices)):
        vertices[i][0] *= scale[0]
        vertices[i][1] *= scale[1]

    # Move os vertices de volta para a posição original
    for i in range(len(vertices)):
        vertices[i] = [vertices[i][0] + center[0], vertices[i][1] + center[1]]
    
    return vertices

def scaleEntityRet(tamanhoQuadrado = [0, 0], verticesMin = [0,0], scale = (1,1)):
    vertices = [verticesMin] + [[verticesMin[0] + tamanhoQuadrado[1], verticesMin[1] + tamanhoQuadrado[1]]]
    #print('escala ma função escalarRetangulo: ', scale)
    #print(vertices)
    #print("teste")
    vertices = scaleEntity(vertices, scale)

    tamanhoQuadrado[0] *= scale[0]
    tamanhoQuadrado[1] *= scale[1]

    return vertices[0], tamanhoQuadrado 

#Função para rotacionar um objeto
def rotateEntity(vertices = [[0,0]], angle = 0):
    # Move os vertices para a origem
    center = getCenter(vertices)
    for i in range(len(vertices)):
        vertices[i] = [vertices[i][0] - center[0], vertices[i][1] - center[1]]

    # Rotaciona os vertices
    for i in range(len(vertices)):
        x = vertices[i][0]
        y = vertices[i][1]
        vertices[i][0] = x * math.cos(angle) - y * math.sin(angle)
        vertices[i][1] = x * math.sin(angle) + y * math.cos(angle)

    # Move os vertices de volta para a posição original
    for i in range(len(vertices)):
        vertices[i] = [vertices[i][0] + center[0], vertices[i][1] + center[1]]
    
    return vertices

    
def getCenter(vertices = [[0,0]]):
    xSum = 0
    ySum = 0
    for vertex in vertices:
        xSum += vertex[0]
        ySum += vertex[1]
    centerX = xSum / len(vertices)
    centerY = ySum / len(vertices)
    return [centerX, centerY]

# # Testando 1
# quadrado = [[0,0], [0,50], [50,50], [50,0]]

# scaleEntity(quadrado, 2)
# print(quadrado)

# Testando 2
# quadrado = scaleEntityRet([50, 50], [0,0], (2, 2))
# print(quadrado)

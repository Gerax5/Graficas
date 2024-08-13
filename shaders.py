import math
from Mathlib import *
import time as t
import random
def vertexShader(vertex, **kwargs): #** = argumentos
    #se lleva a cabo por cada vertice
    #se va a encargar de transformar los vertices
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    viewportMatrix = kwargs["viewportMatrix"]
    
    vt = [vertex[0], vertex[1], vertex[2], 1]

    vt = multiplyMatrixVector(
            multiplyMatrixMatrix(
                multiplyMatrixMatrix(
                    multiplyMatrixMatrix(viewportMatrix, projectionMatrix)
                                        , viewMatrix)
                                        , modelMatrix)
                                        , vt)
    
    #vt = modelMatrix @ vt

    #print(vt)

    #vt = vt.tolist()[0]

    #vt = vt[0]
    
    vt = [vt[0]/vt[3], vt[1]/vt[3], vt[2]/vt[3]]
    
    return vt

def unlitShader(**kwargs):
    # Se lleva a cabo por cada pixel individual
    
    # Obtenemos la informacion requerida
    A, B, C = kwargs["verts"]
    u, v, w = kwargs["bCoords"]
    texture = kwargs["texture"]
    dirLight = kwargs["dirLight"]

    # Sabiendo que las coordenadas de textura
    # estan en la 4ta y 5ta posicion de cada
    # indice del vertice, los obtenemos y
    # y guardamos

    vtA = [A[3], A[4]]
    vtB = [B[3], B[4]]
    vtC = [C[3], C[4]]

        
    # Empezamos siempre con color blanco
    r = 1
    g = 1
    b = 1

    # P = uA + vB + wC
    vtP = [u * vtA[0] + v * vtB[0] + w * vtC[0],
           u * vtA[1] + v * vtB[1] + w * vtC[1]]

    if vtP[0] == 1:
        print("algo algo ")
    
    if texture:
        texColor = texture.getColor(vtP[0], vtP[1])

        if texColor == None:
            return [r,g,b]

        r *= texColor[0]
        g *= texColor[1]
        b *= texColor[2]
    
    # # Para el proposito de mostrar las coordenadas de textura
    # # en accion, las usamos para el color
    # r *= u
    # g *= v
    # b *= w
        
    # Se regresa el color
    return [r,g,b]

def gouradShader(**kwargs):
    # Se lleva a cabo por cada pixel individual
    
    # Obtenemos la informacion requerida
    A, B, C = kwargs["verts"]
    u, v, w = kwargs["bCoords"]
    texture = kwargs["texture"]
    dirLight = kwargs["dirLight"]

    # Sabiendo que las coordenadas de textura
    # estan en la 4ta y 5ta posicion de cada
    # indice del vertice, los obtenemos y
    # y guardamos

    vtA = [A[3], A[4]]
    vtB = [B[3], B[4]]
    vtC = [C[3], C[4]]

    # Sabiendo que los valores de las normales
    # estan en la 7ta, 7ma, 8va posicion
    # de cada vertice los obtenemos y guardamos

    nA = [A[5], A[6], A[7]]
    nB = [B[5], B[6], A[7]]
    nC = [C[5], C[6], A[7]]

    normal = [  u * nA[0] + v * nB[0] + w * nC[0],
                u * nA[1] + v * nB[1] + w * nC[1],
                u * nA[2] + v * nB[2] + w * nC[2] ]
        
    # Empezamos siempre con color blanco
    r = 1
    g = 1
    b = 1

    # P = uA + vB + wC
    vtP = [u * vtA[0] + v * vtB[0] + w * vtC[0],
           u * vtA[1] + v * vtB[1] + w * vtC[1]]
    
    if texture:
        texColor = texture.getColor(vtP[0], vtP[1])

        if texColor == None:
            return [r,g,b]

        r *= texColor[0]
        g *= texColor[1]
        b *= texColor[2]
    
    # intensity = normal DOT -dirLight
    dirLightNegative = [-x for x in dirLight]

    intensity = dotProduct(normal, dirLightNegative)
    intensity = max(0, intensity)
    r *= intensity
    g *= intensity
    b *= intensity
        
    # Se regresa el color
    return [r,g,b]


def flatShader(**kwargs):
    # Se lleva a cabo por cada pixel individual
    
    # Obtenemos la informacion requerida
    A, B, C = kwargs["verts"]
    u, v, w = kwargs["bCoords"]
    texture = kwargs["texture"]
    dirLight = kwargs["dirLight"]

    # Sabiendo que las coordenadas de textura
    # estan en la 4ta y 5ta posicion de cada
    # indice del vertice, los obtenemos y
    # y guardamos

    vtA = [A[3], A[4]]
    vtB = [B[3], B[4]]
    vtC = [C[3], C[4]]

    nA = [A[5], A[6], A[7]]
    nB = [B[5], B[6], A[7]]
    nC = [C[5], C[6], A[7]]

    normal = [  (nA[0]+nB[0]+nC[0])/3, 
                (nA[1]+nB[1]+nC[1])/3, 
                (nA[2]+nB[2]+nC[2])/3]
    

    # normal = [  u * nA[0] + v * nB[0] + w * nC[0],
    #             u * nA[1] + v * nB[1] + w * nC[1],
    #             u * nA[2] + v * nB[2] + w * nC[2] ]
        
    # Empezamos siempre con color blanco
    r = 1
    g = 1
    b = 1

    # P = uA + vB + wC
    vtP = [u * vtA[0] + v * vtB[0] + w * vtC[0],
           u * vtA[1] + v * vtB[1] + w * vtC[1]]
    
    if texture:
        texColor = texture.getColor(vtP[0], vtP[1])

        if texColor == None:
            return [r,g,b]

        r *= texColor[0]
        g *= texColor[1]
        b *= texColor[2]
    
    # intensity = normal DOT -dirLight
    dirLightNegative = [-x for x in dirLight]

    intensity = dotProduct(normal, dirLightNegative)
    intensity = max(0, intensity)
    r *= intensity
    g *= intensity
    b *= intensity
        
    # Se regresa el color
    return [r,g,b]


def toonShader(**kwargs):
    # Se lleva a cabo por cada pixel individual
    
    # Obtenemos la informacion requerida
    A, B, C = kwargs["verts"]
    u, v, w = kwargs["bCoords"]
    texture = kwargs["texture"]
    dirLight = kwargs["dirLight"]

    # Sabiendo que las coordenadas de textura
    # estan en la 4ta y 5ta posicion de cada
    # indice del vertice, los obtenemos y
    # y guardamos

    vtA = [A[3], A[4]]
    vtB = [B[3], B[4]]
    vtC = [C[3], C[4]]

    # Sabiendo que los valores de las normales
    # estan en la 7ta, 7ma, 8va posicion
    # de cada vertice los obtenemos y guardamos

    nA = [A[5], A[6], A[7]]
    nB = [B[5], B[6], A[7]]
    nC = [C[5], C[6], A[7]]

    normal = [  u * nA[0] + v * nB[0] + w * nC[0],
                u * nA[1] + v * nB[1] + w * nC[1],
                u * nA[2] + v * nB[2] + w * nC[2] ]
        
    # Empezamos siempre con color blanco
    r = 1
    g = 1
    b = 1

    # P = uA + vB + wC
    vtP = [u * vtA[0] + v * vtB[0] + w * vtC[0],
           u * vtA[1] + v * vtB[1] + w * vtC[1]]
    
    if texture:
        texColor = texture.getColor(vtP[0], vtP[1])

        if texColor == None:
            return [r,g,b]

        r *= texColor[0]
        g *= texColor[1]
        b *= texColor[2]
    
    # intensity = normal DOT -dirLight
    dirLightNegative = [-x for x in dirLight]

    intensity = dotProduct(normal, dirLightNegative)
    intensity = max(0, intensity)

    if intensity < 0.33:
        intensity = 0.3
    elif intensity < 0.66:
        intensity = 0.6
    else:
        intensity = 1

    r *= intensity
    g *= intensity
    b *= intensity
        
    # Se regresa el color
    return [r,g,b]

def phongShader(**kwargs):
    # Se lleva a cabo por cada pixel individual
    
    # Obtenemos la informacion requerida
    A, B, C = kwargs["verts"]
    u, v, w = kwargs["bCoords"]
    texture = kwargs["texture"]
    dirLight = kwargs["dirLight"]

    # Sabiendo que las coordenadas de textura
    # estan en la 4ta y 5ta posicion de cada
    # indice del vertice, los obtenemos y
    # y guardamos

    vtA = [A[3], A[4]]
    vtB = [B[3], B[4]]
    vtC = [C[3], C[4]]

    # Sabiendo que los valores de las normales
    # estan en la 7ta, 7ma, 8va posicion
    # de cada vertice los obtenemos y guardamos

    nA = [A[5], A[6], A[7]]
    nB = [B[5], B[6], A[7]]
    nC = [C[5], C[6], A[7]]

    normal = [  u * nA[0] + v * nB[0] + w * nC[0],
                u * nA[1] + v * nB[1] + w * nC[1],
                u * nA[2] + v * nB[2] + w * nC[2] ]
        
    # Empezamos siempre con color blanco
    r = 1
    g = 1
    b = 1

    # P = uA + vB + wC
    vtP = [u * vtA[0] + v * vtB[0] + w * vtC[0],
           u * vtA[1] + v * vtB[1] + w * vtC[1]]
    
    if texture:
        texColor = texture.getColor(vtP[0], vtP[1])

        if texColor == None:
            return [r,g,b]

        r *= texColor[0]
        g *= texColor[1]
        b *= texColor[2]
    
    # intensity = normal DOT -dirLight
    dirLightNegative = [-x for x in dirLight]

    intensity = dotProduct(normal, dirLightNegative)
    intensity = max(0, intensity)

    if intensity < 0.33:
        intensity = 0.3
    elif intensity < 0.66:
        intensity = 0.6
    else:
        intensity = 1

    r *= intensity
    g *= intensity
    b *= intensity
        
    # Se regresa el color
    return [r,g,b]

def blueToonShader(**kwargs):
    # Se lleva a cabo por cada pixel individual
    
    # Obtenemos la informacion requerida
    A, B, C = kwargs["verts"]
    u, v, w = kwargs["bCoords"]
    texture = kwargs["texture"]
    dirLight = kwargs["dirLight"]

    # Sabiendo que las coordenadas de textura
    # estan en la 4ta y 5ta posicion de cada
    # indice del vertice, los obtenemos y
    # y guardamos

    vtA = [A[3], A[4]]
    vtB = [B[3], B[4]]
    vtC = [C[3], C[4]]

    # Sabiendo que los valores de las normales
    # estan en la 7ta, 7ma, 8va posicion
    # de cada vertice los obtenemos y guardamos

    nA = [A[5], A[6], A[7]]
    nB = [B[5], B[6], A[7]]
    nC = [C[5], C[6], A[7]]

    normal = [  u * nA[0] + v * nB[0] + w * nC[0],
                u * nA[1] + v * nB[1] + w * nC[1],
                u * nA[2] + v * nB[2] + w * nC[2] ]
        
    # Empezamos siempre con color blanco
    r = 1
    g = 1
    b = 1

    # P = uA + vB + wC
    vtP = [u * vtA[0] + v * vtB[0] + w * vtC[0],
           u * vtA[1] + v * vtB[1] + w * vtC[1]]
    
    if texture:
        texColor = texture.getColor(vtP[0], vtP[1])

        if texColor == None:
            return [r,g,b]

        r *= texColor[0]
        g *= texColor[1]
        b *= texColor[2]
    
    # intensity = normal DOT -dirLight
    dirLightNegative = [-x for x in dirLight]

    intensity = dotProduct(normal, dirLightNegative)
    intensity = max(0, intensity)

    if intensity < 0.33:
        intensity = 0.3
    elif intensity < 0.66:
        intensity = 0.6
    else:
        intensity = 1

    r *= intensity
    g *= intensity
    b *= intensity

    blue = [0.5,0.5,1]

    r *= blue[0]
    g *= blue[1]
    b *= blue[2]
        
    # Se regresa el color
    return [r,g,b]

def glowShader(**kwargs):
    # Se lleva a cabo por cada pixel individual
    
    # Obtenemos la informacion requerida
    A, B, C = kwargs["verts"]
    u, v, w = kwargs["bCoords"]
    texture = kwargs["texture"]
    dirLight = kwargs["dirLight"]
    modelMatrix = kwargs["modelMatrix"]
    camMatrix = kwargs["camMatrix"]

    # Sabiendo que las coordenadas de textura
    # estan en la 4ta y 5ta posicion de cada
    # indice del vertice, los obtenemos y
    # y guardamos

    vtA = [A[3], A[4]]
    vtB = [B[3], B[4]]
    vtC = [C[3], C[4]]

    # Sabiendo que los valores de las normales
    # estan en la 7ta, 7ma, 8va posicion
    # de cada vertice los obtenemos y guardamos

    nA = [A[5], A[6], A[7]]
    nB = [B[5], B[6], A[7]]
    nC = [C[5], C[6], A[7]]

    normal = [  u * nA[0] + v * nB[0] + w * nC[0],
                u * nA[1] + v * nB[1] + w * nC[1],
                u * nA[2] + v * nB[2] + w * nC[2] ]
        
    # Empezamos siempre con color blanco
    r = 1
    g = 1
    b = 1

    # P = uA + vB + wC
    vtP = [u * vtA[0] + v * vtB[0] + w * vtC[0],
           u * vtA[1] + v * vtB[1] + w * vtC[1]]
    
    if texture:
        texColor = texture.getColor(vtP[0], vtP[1])

        if texColor == None:
            return [r,g,b]

        r *= texColor[0]
        g *= texColor[1]
        b *= texColor[2]
    
    # intensity = normal DOT -dirLight
    dirLightNegative = [-x for x in dirLight]

    intensity = dotProduct(normal, dirLightNegative)
    intensity = max(0, intensity)
    r *= intensity
    g *= intensity
    b *= intensity

    # GLOW
    yellowGlow = [1,1,0]

    camForward = [camMatrix[0][2],camMatrix[1][2],camMatrix[2][2]]

    glowIntensity = 1 - dotProduct(normal, camForward)

    glowIntensity = min(1, max(0, glowIntensity))

    r += yellowGlow[0] * glowIntensity
    g += yellowGlow[1] * glowIntensity
    b += yellowGlow[2] * glowIntensity

        
    # Se regresa el color
    return [min(1,r),min(1,g),min(1,b)]

def dissolveShader(**kwargs):
    # Se lleva a cabo por cada pixel individual
    
    # Obtenemos la informacion requerida
    A, B, C = kwargs["verts"]
    u, v, w = kwargs["bCoords"]
    texture = kwargs["texture"]
    dirLight = kwargs["dirLight"]
    #time = t.time()
    time = 0.4

    # Sabiendo que las coordenadas de textura
    # estan en la 4ta y 5ta posicion de cada
    # indice del vertice, los obtenemos y
    # y guardamos

    vtA = [A[3], A[4]]
    vtB = [B[3], B[4]]
    vtC = [C[3], C[4]]

    # Sabiendo que los valores de las normales
    # estan en la 7ta, 7ma, 8va posicion
    # de cada vertice los obtenemos y guardamos

    nA = [A[5], A[6], A[7]]
    nB = [B[5], B[6], A[7]]
    nC = [C[5], C[6], A[7]]

    normal = [  u * nA[0] + v * nB[0] + w * nC[0],
                u * nA[1] + v * nB[1] + w * nC[1],
                u * nA[2] + v * nB[2] + w * nC[2] ]
        
    # Empezamos siempre con color blanco
    r = 1
    g = 1
    b = 1

    # P = uA + vB + wC
    vtP = [u * vtA[0] + v * vtB[0] + w * vtC[0],
           u * vtA[1] + v * vtB[1] + w * vtC[1]]
    
    if texture:
        texColor = texture.getColor(vtP[0], vtP[1])

        if texColor == None:
            return [r,g,b]

        r *= texColor[0]
        g *= texColor[1]
        b *= texColor[2]
    

    noiseValue = (math.sin(vtP[0] * 10.0) * math.sin(vtP[1] * 10.0)) * 0.5 + 0.5

    dissolveThreshold = time % 1.0

    if noiseValue < dissolveThreshold:
        if random.randint(0, 1) == 1:
            return [0,0,0]
        else:
            return [random.random(), random.random(), random.random()] 

    # Se regresa el color
    return [r,g,b]


def pixelationShader(**kwargs):
    A, B, C = kwargs["verts"]
    u, v, w = kwargs["bCoords"]
    texture = kwargs["texture"]
    dirLight = kwargs["dirLight"]
    pixelSize = 0.03 

    # Sabiendo que las coordenadas de textura
    # estan en la 4ta y 5ta posicion de cada
    # indice del vertice, los obtenemos y
    # y guardamos

    vtA = [A[3], A[4]]
    vtB = [B[3], B[4]]
    vtC = [C[3], C[4]]

    # Sabiendo que los valores de las normales
    # estan en la 7ta, 7ma, 8va posicion
    # de cada vertice los obtenemos y guardamos

    nA = [A[5], A[6], A[7]]
    nB = [B[5], B[6], A[7]]
    nC = [C[5], C[6], A[7]]

    normal = [  u * nA[0] + v * nB[0] + w * nC[0],
                u * nA[1] + v * nB[1] + w * nC[1],
                u * nA[2] + v * nB[2] + w * nC[2] ]
        
    # Empezamos siempre con color blanco
    r = 1
    g = 1
    b = 1

    # P = uA + vB + wC
    vtP = [u * vtA[0] + v * vtB[0] + w * vtC[0],
           u * vtA[1] + v * vtB[1] + w * vtC[1]]
    
    if texture:
        # se ajustan las coordenadas para que parezca pixel 
        vtP[0] = (vtP[0] // pixelSize) * pixelSize
        vtP[1] = (vtP[1] // pixelSize) * pixelSize

        texColor = texture.getColor(vtP[0], vtP[1])

        if texColor == None:
            return [r,g,b]

        r *= texColor[0]
        g *= texColor[1]
        b *= texColor[2]
    
    # Se regresa el color
    return [r,g,b]


def wireframeShader(**kwargs):
    # Se lleva a cabo por cada pixel individual
    
    # Obtenemos la informacion requerida
    A, B, C = kwargs["verts"]
    u, v, w = kwargs["bCoords"]
    texture = kwargs["texture"]
    dirLight = kwargs["dirLight"]

    # Sabiendo que las coordenadas de textura
    # estan en la 4ta y 5ta posicion de cada
    # indice del vertice, los obtenemos y
    # y guardamos

    vtA = [A[3], A[4]]
    vtB = [B[3], B[4]]
    vtC = [C[3], C[4]]

    # Sabiendo que los valores de las normales
    # estan en la 7ta, 7ma, 8va posicion
    # de cada vertice los obtenemos y guardamos

    nA = [A[5], A[6], A[7]]
    nB = [B[5], B[6], A[7]]
    nC = [C[5], C[6], A[7]]

    normal = [  u * nA[0] + v * nB[0] + w * nC[0],
                u * nA[1] + v * nB[1] + w * nC[1],
                u * nA[2] + v * nB[2] + w * nC[2] ]
        
    # Empezamos siempre con color blanco
    r = 1
    g = 1
    b = 1

    # P = uA + vB + wC
    vtP = [u * vtA[0] + v * vtB[0] + w * vtC[0],
           u * vtA[1] + v * vtB[1] + w * vtC[1]]
    
    if texture:
        texColor = texture.getColor(vtP[0], vtP[1])

        if texColor == None:
            return [r,g,b]

        r *= texColor[0]
        g *= texColor[1]
        b *= texColor[2]
    

    edgeThreshold = 0.05 
    edgeDist1 = min(u, v, w)
    edgeDist2 = min(1 - u, 1 - v, 1 - w)

    if edgeDist1 < edgeThreshold or edgeDist2 < edgeThreshold:
        return [0, 0, 0]

    return [r,g,b]

def fireShader(**kwargs):
    # Supuestament era un shader de fuego pero lo cambia a colores morados
    def getFireColor(y):
        if y < 0.3:
            return [0.5, 0.5, 1] 
        elif y < 0.6:
            return [0, 0, 1]
        else:
            return [1, 1, 1]

    
    # Obtenemos la informacion requerida
    A, B, C = kwargs["verts"]
    u, v, w = kwargs["bCoords"]
    texture = kwargs["texture"]
    dirLight = kwargs["dirLight"]

    # Sabiendo que las coordenadas de textura
    # estan en la 4ta y 5ta posicion de cada
    # indice del vertice, los obtenemos y
    # y guardamos

    vtA = [A[3], A[4]]
    vtB = [B[3], B[4]]
    vtC = [C[3], C[4]]

    # Sabiendo que los valores de las normales
    # estan en la 7ta, 7ma, 8va posicion
    # de cada vertice los obtenemos y guardamos

    nA = [A[5], A[6], A[7]]
    nB = [B[5], B[6], A[7]]
    nC = [C[5], C[6], A[7]]

    normal = [  u * nA[0] + v * nB[0] + w * nC[0],
                u * nA[1] + v * nB[1] + w * nC[1],
                u * nA[2] + v * nB[2] + w * nC[2] ]
        
    # Empezamos siempre con color blanco
    r = 1
    g = 1
    b = 1

    # P = uA + vB + wC
    vtP = [u * vtA[0] + v * vtB[0] + w * vtC[0],
           u * vtA[1] + v * vtB[1] + w * vtC[1]]
    
    if texture:
        texColor = texture.getColor(vtP[0], vtP[1])

        if texColor == None:
            return [r,g,b]

        r *= texColor[0]
        g *= texColor[1]
        b *= texColor[2]
    
    fireColor = getFireColor(vtP[1])
    noise = random.random() * 0.5 + 0.5 

    r = fireColor[0] * noise
    g = fireColor[1] * noise
    b = fireColor[2] * noise

    # Se regresa el color
    return [r,g,b]

def hologramShader(**kwargs):    
    # Obtenemos la informacion requerida
    A, B, C = kwargs["verts"]
    u, v, w = kwargs["bCoords"]
    texture = kwargs["texture"]
    #Supuestamente con el tiempo cambia
    time = 0.5 

    # Sabiendo que las coordenadas de textura
    # estan en la 4ta y 5ta posicion de cada
    # indice del vertice, los obtenemos y
    # y guardamos

    vtA = [A[3], A[4]]
    vtB = [B[3], B[4]]
    vtC = [C[3], C[4]]

    # P = uA + vB + wC
    vtP = [u * vtA[0] + v * vtB[0] + w * vtC[0],
           u * vtA[1] + v * vtB[1] + w * vtC[1]]
    
    if texture:
        texColor = texture.getColor(vtP[0], vtP[1])

        if texColor == None:
            return [0, 0, 0]

        r, g, b = texColor[0], texColor[1], texColor[2]
    else:
        r, g, b = 0.5, 0.5, 1  

    scanline = (math.sin(vtP[1] * 10.0 + time * 5.0) + 1.0) * 0.5
    r *= scanline
    g *= scanline
    b *= scanline

    fresnel = 1.0 - abs(dotProduct([0, 0, 1], [u, v, w]))
    r += fresnel * 0.3
    g += fresnel * 0.3
    b += fresnel * 0.3

    noise = random.random() * 0.1
    r += noise
    g += noise
    b += noise

    r = min(1, r)
    g = min(1, g)
    b = min(1, b)

    cel = [0.678,  0.847, 0.902]

    r *= cel[0]
    r *= cel[1]
    r *= cel[2]

    return [r, g, b]




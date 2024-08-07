from Mathlib import *
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

def fragmentShader(**kwargs):
    # Se lleva a cabo por cada pixel individual
    
    # Obtenemos la informacion requerida
    A, B, C = kwargs["verts"]
    u, v, w = kwargs["bCoords"]
    texture = kwargs["texture"]

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

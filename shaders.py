from Mathlib import *
def vertexShader(vertex, **kwargs): #** = argumentos
    #se lleva a cabo por cada vertice
    #se va a encargar de transformar los vertices
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    viewportMatrix = kwargs["viewpostMatrix"]
    
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
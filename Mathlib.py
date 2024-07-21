import numpy as np
from math import pi, sin, cos


#Matriz por matriz, matriz por vector, normalizar un vector, magnitud de un vector, matriz de identidad, inversa de una matriz

def multiplyMatrixVector(matrix, vector):
    rows = len(matrix)
    cols= len(matrix[0])
    sizeVector = len(vector)
    
    if cols != sizeVector:
        raise ValueError("El número de columnas de la matriz debe ser igual al tamaño del vector.")

    result_vector = [0 for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result_vector[i] += matrix[i][j] * vector[j]
    
    return result_vector

def multiplyMatrixMatrix(matrix_a, matrix_b):
    rowsA, colsA = len(matrix_a), len(matrix_a[0])
    rowsB, colsB = len(matrix_b), len(matrix_b[0])
    
    if colsA != rowsB:
        raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")
    
    result = [[0 for _ in range(colsB)] for _ in range(rowsA)]
    
    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    
    return result

def normalizeVector(vector):
    magnitude = sum(x**2 for x in vector) ** 0.5
    if magnitude == 0:
        raise ValueError("No se puede normalizar un vector de magnitud cero.")
    return [x / magnitude for x in vector]

def magnitudeVector(vector):
    return sum(x**2 for x in vector) ** 0.5

def identityMatrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def inverseMatrix(matrix):
    n = len(matrix)
    identity = identityMatrix(n)
    #Lo llame temp pero es una matriz aumentada
    temp = [row + identity[i] for i, row in enumerate(matrix)]

    for i in range(n):
        factor = temp[i][i]
        if factor == 0:
            raise ValueError("La matriz no es invertible.")
        for j in range(2 * n):
            temp[i][j] /= factor
        
        for k in range(n):
            if k != i:
                factor = temp[k][i]
                for j in range(2 * n):
                    temp[k][j] -= factor * temp[i][j]

    # Extraer la inversa de la matriz aumentada
    inverse = [row[n:] for row in temp]
    return inverse

def TranslationMatrix(x,y,z):
   return [ [1,0,0,x],
            [0,1,0,y],
            [0,0,1,z],
            [0,0,0,1]
         ]

def ScaleMatrix(x,y,z):
   return[  [x,0,0,0],
            [0,y,0,0],
            [0,0,z,0],
            [0,0,0,1]
         ]

def RotationMatrixX(pitch, yaw, roll):
   #convertir a radianes
   pitch *= pi/180
   yaw *= pi/180
   roll *= pi/180
   
   #creamos la matriz de toracion para eje
   pitchMat = [[1,0,0,0],
               [0,cos(pitch),-sin(pitch),0],
               [0,sin(pitch),cos(pitch),0],
               [0,0,0,1]]

   yawMat = [  [cos(yaw),0,sin(yaw),0],
               [0,1,0,0],
               [-sin(yaw),0,cos(yaw),0],
               [0,0,0,1]
            ]

   rollMat = [ [cos(roll),-sin(roll),0,0],
               [sin(roll),cos(roll),0,0],
               [0,0,1,0],
               [0,0,0,1]
            ]
   
   #return pitchMat * yawMat * rollMat
   return multiplyMatrixMatrix(multiplyMatrixMatrix(pitchMat, yawMat), rollMat)
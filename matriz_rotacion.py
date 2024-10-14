import math
import numpy as np

def matriz_rotacion(alpha, beta, gamma):
    """Define una matriz de rotación a partir de los ángulos alpha, beta y gamma en radianes."""
    # Matriz de rotación en el eje X
    Rx = np.array([
        [1, 0, 0],
        [0, math.cos(alpha), -math.sin(alpha)],
        [0, math.sin(alpha), math.cos(alpha)]
    ])
    
    # Matriz de rotación en el eje Y
    Ry = np.array([
        [math.cos(beta), 0, math.sin(beta)],
        [0, 1, 0],
        [-math.sin(beta), 0, math.cos(beta)]
    ])
    
    # Matriz de rotación en el eje Z
    Rz = np.array([
        [math.cos(gamma), -math.sin(gamma), 0],
        [math.sin(gamma), math.cos(gamma), 0],
        [0, 0, 1]
    ])
    
    # Matriz de rotación completa
    return Rz @ Ry @ Rx

import math
import numpy as np
from funciones_auxiliares import latitud_media, radio_curvatura_meridiano, calcular_V
from matriz_rotacion import matriz_rotacion

def metodo_directo_con_matriz(phi1, phi2, alpha1, alpha2, distance):
    """Calcula las coordenadas X, Y, Z y la latitud y longitud usando el método directo y matrices de rotación."""
    # 1. Calcular la latitud media
    phi_m = latitud_media(phi1, phi2)
    
    # 2. Calcular el radio de curvatura en el meridiano
    M_m = radio_curvatura_meridiano(phi_m)
    
    # 3. Calcular el ángulo de declinación V (ecuación 6.87)
    V = calcular_V(M_m, alpha2)
    
    # 4. Cálculo de las diferencias en coordenadas rectangulares usando el ángulo V
    delta_x = distance * math.cos(alpha1 + V)
    delta_y = distance * math.sin(alpha1 + V)
    delta_z = distance * math.sin(phi_m)
    
    # Crear el vector de desplazamiento en el sistema de referencia original
    delta_vector = np.array([delta_x, delta_y, delta_z])
    
    # 5. Calcular la matriz de rotación con los ángulos (alpha1, alpha2, V)
    rot_matrix = matriz_rotacion(alpha1, alpha2, V)
    
    # 6. Aplicar la rotación al vector de desplazamiento
    rotated_vector = rot_matrix @ delta_vector
    
    # 7. Coordenadas del segundo punto (X2, Y2, Z2) después de la rotación
    X1, Z1 = 0, 0  # Asumimos punto inicial en el origen para simplificación
    X2 = X1 + rotated_vector[0]
    Y2 = rotated_vector[1]
    Z2 = Z1 + rotated_vector[2]
    
    # 8. Calcular latitud y longitud usando tangentes (ecuaciones 6.85 y 6.86)
    phi2 = math.atan(Z2 / ((1 - math.e**2) * math.sqrt(X2**2 + Y2**2)))
    delta_lambda = math.atan(Y2 / X2)
    
    # Convertimos a grados para interpretación
    phi2_deg = math.degrees(phi2)
    delta_lambda_deg = math.degrees(delta_lambda)
    
    return X2, Y2, Z2, phi2_deg, delta_lambda_deg

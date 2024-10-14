import math
from constantes import R, e  # Usa el radio y excentricidad de la Tierra desde constantes.py

def metodo_inverso_gauss(phi1, lambda1, phi2, lambda2):
    """
    Calcula la distancia y los azimuts entre dos puntos en un elipsoide utilizando el método de Gauss.

    Parámetros:
        phi1, lambda1: Latitud y longitud del primer punto (en radianes).
        phi2, lambda2: Latitud y longitud del segundo punto (en radianes).

    Retorna:
        distancia: Distancia entre los dos puntos en metros.
        azimut_directo: Azimut del primer punto hacia el segundo en grados.
        azimut_inverso: Azimut del segundo punto hacia el primero en grados.
    """
    # Cálculo de las diferencias en latitud y longitud
    delta_phi = phi2 - phi1
    delta_lambda = lambda2 - lambda1

    # Calculo de la latitud media
    phi_m = (phi1 + phi2) / 2

    # Cálculo del radio de curvatura en el meridiano y el radio de la curvatura en el prime vertical
    M = R / (1 - e**2 * (math.sin(phi_m) ** 2)) ** 1.5  # Radio en el meridiano
    N = R / math.sqrt(1 - e**2 * (math.sin(phi_m) ** 2))  # Radio en el prime vertical

    # Cálculo de la distancia geodésica aproximada
    distancia = math.sqrt((M * delta_phi) ** 2 + (N * math.cos(phi_m) * delta_lambda) ** 2)

    # Cálculo de los azimuts
    azimut_directo = math.atan2(delta_lambda, delta_phi)  # Azimut directo en radianes
    azimut_inverso = (azimut_directo + math.pi) % (2 * math.pi)  # Azimut inverso en radianes

    # Conversión de los azimuts a grados
    azimut_directo = math.degrees(azimut_directo)
    azimut_inverso = math.degrees(azimut_inverso)

    return distancia, azimut_directo, azimut_inverso

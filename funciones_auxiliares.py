import math
from constantes import R, e

def latitud_media(phi1, phi2):
    """Calcula la latitud media entre dos puntos."""
    return (phi1 + phi2) / 2

def radio_curvatura_meridiano(phi_m):
    """Calcula el radio de curvatura en el meridiano en la latitud media."""
    return R / math.sqrt(1 - (e**2) * (math.sin(phi_m)**2))

def calcular_V(M, alpha2):
    """Calcula el ángulo de declinación V usando la ecuación (6.87)."""
    V = -M / (2 * R) * (1 + e**2 * math.cos(alpha2)**2)
    return V

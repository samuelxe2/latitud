import math
from metodo_directo import metodo_directo_con_matriz
from metodo_inverso_gauss import metodo_inverso_gauss

def menu():
    print("Seleccione el método:")
    print("1. Método Directo")
    print("2. Método Inverso de Gauss")
    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        # Método directo
        phi1 = math.radians(float(input("Ingrese la latitud inicial (en grados): ")))
        phi2 = math.radians(float(input("Ingrese la latitud final (en grados): ")))
        alpha1 = math.radians(float(input("Ingrese el azimut inicial (en grados): ")))
        alpha2 = math.radians(float(input("Ingrese el ángulo del segundo punto (en grados): ")))
        distance = float(input("Ingrese la distancia (en metros): "))

        # Cálculo de las coordenadas y latitud/longitud del segundo punto con matriz de rotación
        X2, Y2, Z2, lat2, lon2 = metodo_directo_con_matriz(phi1, phi2, alpha1, alpha2, distance)
        print("Coordenadas obtenidas (Directo con Matriz):")
        print(f"X2: {X2} m, Y2: {Y2} m, Z2: {Z2} m")
        print(f"Latitud: {lat2}°, Longitud: {lon2}°")

    elif opcion == "2":
        # Método inverso de Gauss
        phi1 = math.radians(float(input("Ingrese la latitud del primer punto (en grados): ")))
        lambda1 = math.radians(float(input("Ingrese la longitud del primer punto (en grados): ")))
        phi2 = math.radians(float(input("Ingrese la latitud del segundo punto (en grados): ")))
        lambda2 = math.radians(float(input("Ingrese la longitud del segundo punto (en grados): ")))

        # Cálculo de la distancia y azimut usando el método inverso de Gauss
        distancia, azimut_directo, azimut_inverso = metodo_inverso_gauss(phi1, lambda1, phi2, lambda2)
        print("Resultados del Método Inverso de Gauss:")
        print(f"Distancia: {distancia} m")
        print(f"Azimut Directo: {azimut_directo}°")
        print(f"Azimut Inverso: {azimut_inverso}°")

    else:
        print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

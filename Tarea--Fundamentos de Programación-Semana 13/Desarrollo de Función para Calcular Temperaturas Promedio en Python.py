def calcular_temperatura_promedio(datos):
    """
    Calcula la temperatura promedio de cada ciudad durante un período de tiempo.

    Parámetros:
    datos (dict): Un diccionario donde las claves son los nombres de las ciudades
                  y los valores son listas de listas que representan las temperaturas
                  de cada semana.

    Retorna:
    dict: Un diccionario con las ciudades como claves y sus temperaturas promedio como valores.
    """
    promedios = {}

    for ciudad, semanas in datos.items():
        # Sumar todas las temperaturas de todas las semanas
        total_temperaturas = sum(sum(semana) for semana in semanas)

        # Calcular el número total de mediciones
        total_mediciones = sum(len(semana) for semana in semanas)

        # Calcular el promedio
        if total_mediciones > 0:
            promedios[ciudad] = total_temperaturas / total_mediciones
        else:
            promedios[ciudad] = 0

    return promedios


# Ejemplo de datos de temperaturas para 3 ciudades durante 4 semanas
datos_temperaturas = {
    "Puerto Asis": [[22, 24, 23, 25], [21, 20, 22, 24], [23, 25, 26, 24], [20, 22, 21, 23]],
    "Villavicencio": [[18, 19, 20, 18], [17, 18, 19, 20], [19, 20, 21, 22], [18, 19, 20, 21]],
    "Cartagena": [[30, 31, 32, 33], [29, 30, 31, 32], [31, 32, 33, 34], [30, 31, 32, 33]]
}

# Calcular los promedios
promedios = calcular_temperatura_promedio(datos_temperaturas)

# Mostrar los resultados
for ciudad, promedio in promedios.items():
    print(f"La temperatura promedio en {ciudad} es: {promedio:.2f}°C")
def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad a partir de una lista de temperaturas semanales.

    :param temperaturas: Lista de listas, donde cada lista contiene las temperaturas semanales de una ciudad.
                         Por ejemplo: [[20, 22, 24, 21], [15, 18, 20, 22], [25, 26, 24, 23], [10, 12, 14, 16], [30, 32, 31, 29]]
    :return: Lista de temperaturas promedio para cada ciudad.
    """

    # Lista para almacenar los promedios de cada ciudad
    promedios = []

    # Iterar sobre cada ciudad en los datos de temperaturas
    for ciudad in temperaturas:
        # Verificar si la lista de temperaturas de la ciudad está vacía
        if not ciudad:
            # Añadir None en caso de listas vacías para manejar el caso adecuadamente
            promedios.append(None)
            continue

        # Calcular el promedio de temperaturas para la ciudad
        promedio = sum(ciudad) / len(ciudad)
        # Añadir el promedio calculado a la lista de promedios
        promedios.append(promedio)

    # Devolver la lista de promedios de temperaturas
    return promedios


# Ejemplo de uso:
datos_temperaturas = [
    [20, 22, 24, 21],  # Temperaturas para la ciudad 1
    [15, 18, 20, 22],  # Temperaturas para la ciudad 2
    [25, 26, 24, 23],  # Temperaturas para la ciudad 3
    [10, 12, 14, 16],  # Temperaturas para la ciudad 4
    [30, 32, 31, 29]  # Temperaturas para la ciudad 5
]

# Llamar a la función para calcular los promedios
promedios = calcular_temperatura_promedio(datos_temperaturas)
print(promedios)  # Salida esperada: [21.75, 18.75, 24.5, 13.0, 30.5]

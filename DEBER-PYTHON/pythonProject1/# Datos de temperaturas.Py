datos_temperaturas = {
    "Santo Domingo": [[28, 29, 30, 28], [27, 26, 28, 29], [29, 30, 31, 30], [26, 27, 28, 29]],
    "Quito": [[15, 16, 17, 15], [14, 13, 15, 16], [16, 17, 18, 17], [13, 14, 15, 16]],
    "Loja": [[20, 21, 22, 20], [19, 18, 20, 21], [21, 22, 23, 22], [18, 19, 20, 21]]
}
def calcular_temperatura_promedio(datos_temperaturas):
    promedios = {}  # Diccionario para almacenar los promedios de cada ciudad

    # Iterar sobre cada ciudad y sus datos de temperaturas
    for ciudad, semanas in datos_temperaturas.items():
        total_temperaturas = 0  # Acumulador para la suma de temperaturas
        total_mediciones = 0    # Contador para el número total de mediciones

        # Iterar sobre las semanas y las temperaturas de cada semana
        for semana in semanas:
            total_temperaturas += sum(semana)  # Sumar las temperaturas de la semana
            total_mediciones += len(semana)    # Contar el número de mediciones

        # Calcular el promedio de la ciudad
        promedio = total_temperaturas / total_mediciones
        promedios[ciudad] = round(promedio, 2)  # Redondear a 2 decimales

    return promedios
# Datos de temperaturas
datos_temperaturas = {
    "Santo Domingo": [[28, 29, 30, 28], [27, 26, 28, 29], [29, 30, 31, 30], [26, 27, 28, 29]],
    "Quito": [[15, 16, 17, 15], [14, 13, 15, 16], [16, 17, 18, 17], [13, 14, 15, 16]],
    "Loja": [[20, 21, 22, 20], [19, 18, 20, 21], [21, 22, 23, 22], [18, 19, 20, 21]]
}

# Calcular promedios
resultados = calcular_temperatura_promedio(datos_temperaturas)

# Mostrar resultados
for ciudad, promedio in resultados.items():
    print(f"La temperatura promedio en {ciudad} es: {promedio}°C")
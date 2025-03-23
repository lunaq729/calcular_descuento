# Crear una matriz 3D para almacenar temperaturas diarias
# Dimensiones: [Ciudades][Días de la semana][Semanas]
temperaturas = [
    # Ciudad 1
    [
        [25, 26, 27, 28, 29, 30, 31],  # Semana 1 (Lunes a Domingo)
        [24, 25, 26, 27, 28, 29, 30]   # Semana 2
    ],
    # Ciudad 2
    [
        [20, 21, 22, 23, 24, 25, 26],  # Semana 1 (Martes a Sabado)
        [19, 20, 21, 22, 23, 24, 25]   # Semana 2
    ],
    # Ciudad 3
    [
        [30, 31, 32, 33, 34, 35, 36],  # Semana 1( Miercoles a Viernes)
        [29, 30, 31, 32, 33, 34, 35]   # Semana 2
    ]
]

# Nombres de las ciudades y días de la semana
ciudades = ["Ciudad 1 Santo Domingo", "Ciudad 2 Quito", "Ciudad 3 Loja"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Calcular el promedio de temperaturas por ciudad y semana
for i in range(len(temperaturas)):  # Recorre ciudades
    for k in range(len(temperaturas[i])):  # Recorre semanas
        suma_temperaturas = 0
        for j in range(len(temperaturas[i][k])):  # Recorre días de la semana
            suma_temperaturas += temperaturas[i][k][j]
        
        # Calcular el promedio
        promedio = suma_temperaturas / len(temperaturas[i][k])
        
        # Mostrar el resultado
        print(f"Promedio de temperaturas en {ciudades[i]}, Semana {k + 1}: {promedio:.2f}°C")
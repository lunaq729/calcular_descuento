
# Definimos los nombres de las ciudades y los días
ciudades = ["Ciudad Santo Domingo", "Ciudad Guayaquil", "Ciudad Loja"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4  # Por ejemplo, 4 semanas

# Creamos la matriz 3D: [ciudad][día][semana]
# Usamos valores de temperatura aleatorios entre 15°C y 35°C
matriz_temperaturas = [[[random.randint(15, 35) for _ in range(semanas)]
                         for _ in range(len(dias))]
                         for _ in range(len(ciudades))]

# Mostramos los datos generados (opcional)
print("📊 MATRIZ DE TEMPERATURAS GENERADA:\n")
for i in range(len(ciudades)):
    print(f"🌆 {ciudades[i]}")
    for s in range(semanas):
        print(f"  Semana {s+1}: ", end="")
        for d in range(len(dias)):
            print(f"{dias[d]}: {matriz_temperaturas[i][d][s]}°C", end=", ")
        print()
    print()

# Calculamos el promedio por ciudad y semana
print("📈 PROMEDIO DE TEMPERATURAS POR CIUDAD Y SEMANA:\n")
for i in range(len(ciudades)):
    print(f"🌆 {ciudades[i]}")
    for s in range(semanas):
        suma_temperaturas = 0
        for d in range(len(dias)):
            suma_temperaturas += matriz_temperaturas[i][d][s]
        promedio = suma_temperaturas / len(dias)
        print(f"  Semana {s+1}: Promedio = {promedio:.2f}°C")
    print()

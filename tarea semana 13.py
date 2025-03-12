#elfe

# Definir dimensiones
ciudades = ["ambato", "quito", "cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 4

# Crear la matriz 3D con temperaturas aleatorias entre 10 y 35 grados
matriz_temperaturas = [[[random.uniform(10, 35) for _ in dias_semana] for _ in range(num_semanas)] for _ in ciudades]

# Calcular y mostrar el promedio de temperaturas para cada ciudad por semana
for i, ciudad in enumerate(ciudades):
    print(f"Promedios semanales de temperatura en {ciudad}:")
    for semana in range(num_semanas):
        promedio = sum(matriz_temperaturas[i][semana]) / len(dias_semana)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
    print()


# Laberinto representado como una matriz
laberinto = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", "S", " ", "#", " ", "E", "#"],
    ["#", " ", " ", "#", " ", "#", "#"],
    ["#", "#", " ", " ", " ", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]

# Marcas del camino: cuántas veces hemos pasado por cada celda
marcas = [[0 for _ in fila] for fila in laberinto]

# Direcciones: arriba, abajo, izquierda, derecha
direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def encontrar_inicio(laberinto):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] == "S":
                return i, j
    return None

def es_valido(fila, columna):
    return (
        0 <= fila < len(laberinto) and
        0 <= columna < len(laberinto[0]) and
        laberinto[fila][columna] != "#"
    )

def tremaux(fila, columna):
    if laberinto[fila][columna] == "E":
        return True  # ¡Llegamos a la salida!

    marcas[fila][columna] += 1  # Marcamos esta celda

    for df, dc in direcciones:
        nueva_fila = fila + df
        nueva_columna = columna + dc

        if es_valido(nueva_fila, nueva_columna):
            if marcas[nueva_fila][nueva_columna] < 2:
                if tremaux(nueva_fila, nueva_columna):
                    return True

    return False  # Retrocedemos si no hay camino

# Ejecutar el algoritmo
inicio = encontrar_inicio(laberinto)
if inicio:
    if tremaux(*inicio):
        print("¡Camino encontrado hasta la salida!")
    else:
        print("No hay camino posible a la salida.")
else:
    print("No se encontró el punto de inicio.")

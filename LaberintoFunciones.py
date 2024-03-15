import random

# 15/03/2024
"""
FERNANDA NICOLE GARCÍA MELENDREZ
JESSICA ABRIL QUINTERO CASTILLO
ALEJANDRO COSTICH SANDOVAL

"""
# oalqepfl

FILAS = 5
COLUMNAS = 5
META_FILA = FILAS - 1
META_COLUMNA = COLUMNAS - 1

def inicializar_laberinto():
    laberinto = [[False] * COLUMNAS for _ in range(FILAS)]
    laberinto[META_FILA][META_COLUMNA] = True  # Meta
    return laberinto

def imprimir_laberinto(laberinto, fila_jugador, columna_jugador):
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if i == fila_jugador and j == columna_jugador:
                print("X ", end='')  # Jugador
            elif laberinto[i][j]:
                print("O ", end='')  # Meta
            else:
                print(". ", end='')  # Espacio vacío
        print()

def verificar_meta(fila_jugador, columna_jugador):
    return fila_jugador == META_FILA and columna_jugador == META_COLUMNA

def obtener_movimiento(cScheme):
    return input(f"\nIngrese su siguiente movimiento ({cScheme[0]}: arriba, {cScheme[1]}: abajo, {cScheme[2]}: izquierda, {cScheme[3]}: derecha)" )

def mover_jugador(fila_jugador, columna_jugador, movimiento, cScheme):
    if movimiento == cScheme[0] and fila_jugador > 0:
        fila_jugador -= 1
    elif movimiento == cScheme[1] and fila_jugador < FILAS - 1:
        fila_jugador += 1
    elif movimiento == cScheme[2] and columna_jugador > 0:
        columna_jugador -= 1
    elif movimiento == cScheme[3] and columna_jugador < COLUMNAS - 1:
        columna_jugador += 1
    else:
        print("Movimiento no válido.")
    return fila_jugador, columna_jugador

def defineControls(cScheme):
    cScheme[0] = str(input('Ingrese tecla para moverse hacia arriba.'))
    cScheme[1] = str(input('Ingrese tecla para moverse hacia abajo.'))
    cScheme[2] = str(input('Ingrese tecla para moverse hacia la izquierda.'))
    cScheme[3] = str(input('Ingrese tecla para moverse hacia la derecha.'))

    return cScheme

def main():
    cScheme = [None] * 4 # array is initialized
    defineControls(cScheme)

    laberinto = inicializar_laberinto()
    fila_jugador, columna_jugador = 0, 0

    while True:
        imprimir_laberinto(laberinto, fila_jugador, columna_jugador)
        if verificar_meta(fila_jugador, columna_jugador):
            print("\n¡Has alcanzado la meta! ¡Felicidades!")
            break

        movimiento = obtener_movimiento(cScheme)
        fila_jugador, columna_jugador = mover_jugador(fila_jugador, columna_jugador, movimiento, cScheme)

if __name__ == "__main__":
    main()

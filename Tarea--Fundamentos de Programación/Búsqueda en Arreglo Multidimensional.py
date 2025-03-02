def bubble_sort(fila):
    """Ordena una fila utilizando el algoritmo Bubble Sort."""
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                # Intercambiar si el elemento encontrado es mayor que el siguiente
                fila[j], fila[j+1] = fila[j+1], fila[j]

def ordenar_fila(matriz, fila_a_ordenar):
    """Ordena una fila específica de la matriz."""
    if 0 <= fila_a_ordenar < len(matriz):
        bubble_sort(matriz[fila_a_ordenar])
    else:
        print("Índice de fila fuera de rango.")

def mostrar_matriz(matriz):
    """Muestra la matriz en formato legible."""
    for fila in matriz:
        print(fila)

def main():
    # Definimos una matriz 3x3
    matriz = [
        [9, 2, 5],
        [4, 8, 1],
        [7, 3, 6]
    ]

    print("Matriz original:")
    mostrar_matriz(matriz)

    # Pedimos al usuario que introduzca el índice de la fila a ordenar
    fila_a_ordenar = int(input("Introduce el índice de la fila a ordenar (0-2): "))

    # Ordenamos la fila especificada
    ordenar_fila(matriz, fila_a_ordenar)

    print("\nMatriz después de ordenar la fila:")
    mostrar_matriz(matriz)

if __name__ == "__main__":
    main()
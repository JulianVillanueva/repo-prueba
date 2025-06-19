def partition(arr, low, high):
    """
    Esta función toma el último elemento como pivote, lo coloca en su
    posición correcta en el arreglo ordenado, y sitúa todos los menores
    a su izquierda y los mayores a su derecha.
    
    Args:
        arr (list): El arreglo a particionar.
        low (int): El índice de inicio.
        high (int): El índice de fin.
        
    Returns:
        int: El índice donde el pivote ha sido colocado.
    """
    # Elegimos el último elemento como pivote.
    pivot = arr[high]
    
    # 'i' será el índice del elemento más pequeño encontrado hasta ahora.
    # Empezamos asumiendo que está justo antes del inicio del arreglo.
    i = low - 1
    
    # Recorremos el arreglo desde 'low' hasta 'high - 1' (sin incluir el pivote).
    for j in range(low, high):
        # Si el elemento actual es menor o igual que el pivote...
        if arr[j] <= pivot:
            # ...incrementamos el índice 'i' y hacemos un intercambio (swap).
            # Esto mueve el elemento pequeño a la sección de "menores".
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            
    # Al final del bucle, todos los elementos menores que el pivote están
    # a la izquierda de 'i'. Ahora colocamos el pivote en su lugar correcto.
    # Hacemos un swap entre arr[i + 1] y el pivote (arr[high]).
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Retornamos el índice donde ahora se encuentra el pivote.
    return i + 1

def quick_sort_recursive(arr, low, high):
    """
    La función principal que implementa Quicksort.
    
    Args:
        arr (list): Arreglo a ordenar.
        low (int): Índice de inicio.
        high (int): Índice de fin.
    """
    if low < high:
        # 'pi' es el índice de partición. arr[pi] ya está en su lugar correcto.
        pi = partition(arr, low, high)
        
        # Ordenamos de forma recursiva los elementos antes y después de la partición.
        quick_sort_recursive(arr, low, pi - 1)  # Sub-arreglo izquierdo
        quick_sort_recursive(arr, pi + 1, high) # Sub-arreglo derecho

def quick_sort(arr):
    """
    Función de ayuda (wrapper) para facilitar el llamado inicial.
    """
    if not arr:
        return []
    quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr

# --- Ejemplo de Uso ---
mi_lista = [10, 7, 8, 9, 1, 5, 3, 6, 2, 4]
print(f"Lista original: {mi_lista}")

# Llamamos a la función principal para ordenar la lista
quick_sort(mi_lista)

print(f"Lista ordenada: {mi_lista}")

# Otro ejemplo
lista_desordenada = [64, 34, 25, 12, 22, 11, 90, 5]
print(f"\nLista original: {lista_desordenada}")
quick_sort(lista_desordenada)
print(f"Lista ordenada: {lista_desordenada}")
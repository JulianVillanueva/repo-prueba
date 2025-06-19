def segundo(numeros: list) -> int | None:
    """
    Encuentra el segundo número más grande usando sets y ordenamiento.
    Retorna el número o None si no hay un segundo más grande.
    """
    # 1. Eliminar duplicados convirtiendo a un conjunto (set)
    numeros_unicos = list(set(numeros))
    
    # 2. Manejar casos donde no puede haber un segundo más grande
    if len(numeros_unicos) < 2:
        return None
        
    # 3. Ordenar la lista de únicos de mayor a menor
    numeros_unicos.sort(reverse=True)
    
    # 4. El segundo más grande es el elemento en el índice 1
    return numeros_unicos[1]

# --- Ejemplos de uso ---
lista1 = [1, 5, 2, 8, 9, 9, 3]
lista2 = [10, 10, 8, 7]
lista3 = [5, 5, 5] # No hay segundo más grande
lista4 = [10]      # No hay segundo más grande

print(f"Lista: {lista1} -> Segundo más grande: {segundo(lista1)}")
print(f"Lista: {lista2} -> Segundo más grande: {segundo(lista2)}")
print(f"Lista: {lista3} -> Segundo más grande: {segundo(lista3)}")
print(f"Lista: {lista4} -> Segundo más grande: {segundo(lista4)}")
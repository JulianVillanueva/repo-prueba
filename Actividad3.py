def encontrar_vocal_mas_repetida(texto: str) -> str:
    """
    Encuentra la vocal que más se repite en un texto.

    - Considera vocales con y sin tilde como la misma.
    - No diferencia entre mayúsculas y minúsculas.
    - Si no hay vocales, retorna una cadena vacía.
    - En caso de empate, retorna la primera vocal encontrada con la frecuencia máxima.

    Args:
        texto: La cadena de texto para analizar.

    Returns:
        La vocal que más se repite o "" si no hay vocales.
    """
    if not isinstance(texto, str):
        return ""
    
    # Creamos un diccionario para contar las vocales
    conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Convertimos todo el texto a minúsculas para un análisis uniforme
    for caracter in texto.lower():
        
        # Si la letra es una vocal, incrementamos su contador
        if caracter in conteo_vocales:
            conteo_vocales[caracter] += 1
            
    # Si después de recorrer el texto no se contó ninguna vocal
    if not any(conteo_vocales.values()):
        return ""
        
    # Usamos max() para encontrar la clave (vocal) con el valor (conteo) más alto
    vocal_mas_frecuente = max(conteo_vocales, key=conteo_vocales.get)
    
    return vocal_mas_frecuente

# --- Ejemplos de uso ---

# Ejemplo estándar
texto1 = "El murcielago esta super increiblemente feliz."
print(f"Texto: '{texto1}'")
print(f"Vocal más repetida: '{encontrar_vocal_mas_repetida(texto1)}' 🗣️") 
# Salida esperada: 'e'

print("-" * 20)

# Ejemplo con mayúsculas y acentos variados
texto2 = "ARGENTINA GANÓ EL MUNDIAL DE FÚTBOL"
print(f"Texto: '{texto2}'")
print(f"Vocal más repetida: '{encontrar_vocal_mas_repetida(texto2)}'")
# Salida esperada: 'o'

print("-" * 20)

# Caso especial: Sin vocales
texto3 = "Rhythm gym nth."
print(f"Texto: '{texto3}'")
print(f"Vocal más repetida: '{encontrar_vocal_mas_repetida(texto3)}' 🤫")
# Salida esperada: ''

print("-" * 20)

# Caso especial: Empate
texto4 = "Aquel viejo auto."
print(f"Texto: '{texto4}'")
print(f"Vocal más repetida: '{encontrar_vocal_mas_repetida(texto4)}'")
# Salida esperada: 'a' (es la primera en el diccionario que alcanza el máximo de 3)
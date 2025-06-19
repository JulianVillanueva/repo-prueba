import re

def es_palindromo_simple(texto: str) -> bool:
    """
    Verifica si un texto es un palíndromo de la forma más directa.
    """
    texto_limpio = ""
    for caracter in texto:
        if caracter.isalnum():
            texto_limpio += caracter.lower()
    
    # 2. Invertir la cadena usando slicing [::-1]
    texto_invertido = texto_limpio[::-1]
    
    # 3. Comparar y retornar el resultado
    return texto_limpio == texto_invertido

# --- Ejemplos de uso ---
print(f"'Anita lava la tina' -> {es_palindromo_simple('Anita lava la tina')}")
print(f"'A man, a plan, a canal: Panama' -> {es_palindromo_simple('A man, a plan, a canal: Panama')}")
print(f"'Hola mundo' -> {es_palindromo_simple('Hola mundo')}")

# Palabras palindromo: somos, reconocer, sometemos, arenera, salas
# Frases: "La ruta nos aportó otro paso natural", "Se van sus naves", "Amo la paloma", "Yo hago yoga hoy", "¿Acaso hubo búhos acá?"
# taco cat, racecar

"""# 1. Limpiar el texto usando expresiones regulares para quitar todo lo que no sea letra o número
    texto_limpio = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()"""
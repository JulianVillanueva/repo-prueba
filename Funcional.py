# Solución tradicional (con bucle for)
numeros = [1, 2, 3, 4, 5]
cuadrados = []
for n in numeros:
    cuadrados.append(n**2)
print(f"Con bucle for: {cuadrados}")


# Solución funcional (con map y lambda)
# lambda n: n**2 es una función anónima que toma n y devuelve n al cuadrado.
cuadrados_funcional = list(map(lambda n: n**2, numeros))
print(f"Con map y lambda: {cuadrados_funcional}")

# La forma más "Pythónica" (con list comprehension), que es muy funcional en espíritu
cuadrados_pythonic = [n**2 for n in numeros]
print(f"Con List Comprehension: {cuadrados_pythonic}")

lista_nombres = ["Alice", "Bob", "Charlie", "David", "Eve"]
lista_nombres_mayusculas = list(map(lambda n: n.upper(), lista_nombres))
print(f"Con map y lambda: {lista_nombres_mayusculas}")

lista_precios = [50, 26, 76, 90, 22, 18]
lista_precios_iva = list(map(lambda p: p * 0.19, lista_precios))

# filter

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

# Solución tradicional
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
print(f"Con bucle for: {pares}")

# Solución funcional (con filter y lambda)
# lambda n: n % 2 == 0 devuelve True si el número es par.
pares_funcional = list(filter(lambda n: n % 2 == 0, numeros))
print(f"Con filter y lambda: {pares_funcional}")

# La forma más "Pythónica"
pares_pythonic = [n for n in numeros if n % 2 == 0]
print(f"Con List Comprehension: {pares_pythonic}")

lista_palabras = ["mouse", "monitor", "microfono", "teclado", "parlante"]
cinco_letras = list(filter(lambda p: p.len() > 4, lista_palabras))
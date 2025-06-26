print('Rama Jorge')

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        productos = []

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}"

print('Esto solo lo hizo Jorge')

class Cliente:
    def __init__(self, nombre, cedula, telefono, correo):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"Cliente: {self.nombre}, Cedula: {self.cedula}, Telefono: {self.telefono}, Correo: {self.correo}"

print('Firma dev2')

def menu():
    print('Bienvenido a la tienda, seleccione una opcin:')
    print('1. Añadir producto')
    print('2. Ver productos')
    print('3. Salir')
    opcion = int(input('Opcion: '))
    return opcion

def main():
    productos = []
    while True:
        opcion = menu()
        if opcion == 1:
            nombre = input('Ingrese el nombre del producto: ')
            precio = float(input('Ingrese el precio del producto: '))
            producto = Producto(nombre, precio)
            productos.append(producto)
        elif opcion == 2:
            for producto in productos:
                print(producto)
        elif opcion == 3:
            break
        else:
            print('Opcion no valida')
    print('Gracias por visitarnos')

if __name__ == '__main__':
    main()

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

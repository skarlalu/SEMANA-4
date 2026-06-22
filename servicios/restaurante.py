class Restaurante:
    def __init__(self, nombre_restaurante):
        self.nombre_restaurante = nombre_restaurante
        self.lista_productos = []
        self.lista_clientes = []

    def registrar_producto(self, producto):
        self.lista_productos.append(producto)
        print(f"✔ Producto registrado: {producto.nombre}")

    def registrar_cliente(self, cliente):
        self.lista_clientes.append(cliente)
        print(f"✔ Cliente registrado: {cliente.nombre} en mesa {cliente.mesa}")

    def mostrar_estado(self):
        print(f"\n--- ESTADO DE: {self.nombre_restaurante.upper()} ---")
        
        print("\n[ Menú Disponible ]")
        if not self.lista_productos:
            print("No hay productos registrados.")
        for prod in self.lista_productos:
            print(f" * {prod}") # Aquí se ejecuta automáticamente el __str__ de Producto

        print("\n[ Clientes Atendidos ]")
        if not self.lista_clientes:
            print("No hay clientes en el restaurante.")
        for cli in self.lista_clientes:
            print(f" * {cli}") # Aquí se ejecuta automáticamente el __str__ de Cliente
        print("-" * 40)
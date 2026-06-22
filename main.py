from modelos.producto import Producto  
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Punto de arranque principal del programa
if __name__ == "__main__":
    # 1. Crear el servicio principal (el restaurante)
    mi_restaurante = Restaurante("Sabores de Mi Tierra")

    print("=== REGISTRANDO INFORMACIÓN ===")
    # 2. Crear objetos de la clase Producto y agregarlos al restaurante
    plato1 = Producto("Ceviche Mixto", 12.50)
    plato2 = Producto("Seco de Pollo", 6.00)
    bebida1 = Producto("Jarra de Chicha", 3.50)

    mi_restaurante.registrar_producto(plato1)
    mi_restaurante.registrar_producto(plato2)
    mi_restaurante.registrar_producto(bebida1)

    print("\n===============================")
    # 3. Crear objetos de la clase Cliente y asignarlos a una mesa
    cliente1 = Cliente("Carlos Mendoza", 4)
    cliente2 = Cliente("Ana Rodríguez", 2)

    mi_restaurante.registrar_cliente(cliente1)
    mi_restaurante.registrar_cliente(cliente2)

    # 4. Mostrar de forma organizada la información final en consola
    mi_restaurante.mostrar_estado()
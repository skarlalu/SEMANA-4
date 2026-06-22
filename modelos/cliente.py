class Cliente:
    def __init__(self, nombre, mesa):
        self.nombre = nombre
        self.mesa = mesa
    def __str__(self):
        return f"Cliente: {self.nombre} (Mesa {self.mesa})"
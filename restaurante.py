class Restaurante:
    def __init__(self, nombre, tipo_comida):
        self.nombre = nombre
        self.tipo_comida = tipo_comida

    def describir_restaurante(self):
        print("Restaurante:", self.nombre)
        print("Comida:", self.tipo_comida)

    def abrir_restaurante(self):
        print("El restaurante está abierto.")
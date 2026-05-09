class Gato():
    def __init__(self, nombre, color_pelo, color_ojos, cansancio, hambre):
        self.nombre = nombre
        self.color_pelo = color_pelo
        self.color_ojos = color_ojos
        self.cansancio = cansancio
        self.hambre = hambre

    def comer(self):
        print("El gato esta comiendo")

    def dormir(self):
        print("El gato esta comiendo")

    def jugar(self):
        print("El gato esta jugando")

    def acariciar(self):
        print("El gato esta siendo acariciado")

gato1 = Gato("Paco", "blanco", "negro", "")


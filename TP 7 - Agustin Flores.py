"""EJERCICIO 1
1. Escribir una clase llamada Rectángulo que contenga una base y una altura
2. Que contenga un método que devuelva el área del rectángulo."""

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
"""EJERCICIO 2
Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener
como miembros:
1. Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
2. Un atributo para el estado (lleno o vacío).
3. Un atributo n, que indica la cantidad máxima de cebadas.
4. Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
5. Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
6. Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
“Advertencia: el mate está lavado.” pero no se debe lanzar una excepción."""

class Mate:
    def __init__(self, n):
        self.cebadas = n
        self.lleno = False

    def cebar(self):
        if self.lleno:
            print("¡Cuidado! ¡Te quemaste!")
        else:
            self.lleno = True

    def beber(self):
        if not self.lleno:
            print("¡El mate está vacío!")
        else:
            self.lleno = False

            if self.cebadas > 0:
                self.cebadas -= 1
            else:
                print("Advertencia: el mate está lavado.")

"""EJERCICIO 3
Botella y Sacacorchos
1. Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
2. Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
destapada.
3. Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
sacacorchos ya contiene un corcho.
4. Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
un corcho."""

class Corcho:
    def __init__(self, bodega):
        self.bodega = bodega


class Botella:
    def __init__(self, corcho):
        self.corcho = corcho


class Sacacorchos:
    def __init__(self):
        self.corcho = None

    def destapar(self, botella):

        if botella.corcho is None:
            print("La botella ya está destapada.")

        elif self.corcho is not None:
            print("El sacacorchos ya tiene un corcho.")

        else:
            self.corcho = botella.corcho
            botella.corcho = None
            print("Botella destapada.")

    def limpiar(self):

        if self.corcho is None:
            print("No hay corcho en el sacacorchos.")

        else:
            self.corcho = None
            print("Sacacorchos limpio.")

"""EJERCICIO 4
1. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos: restaurante_nombre y tipo_comida.
2. Cree un método describir_restaurante() que muestre estas piezas de información, y un método abrir_restaurante()
que muestre un mensaje indicando que el restaurante ahora está abierto.
3. Luego cree una clase Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que
almacene una lista de los sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
al método. """

class Restaurante:
    def __init__(self, restaurante_nombre, tipo_comida):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_comida = tipo_comida

    def describir_restaurante(self):
        print("Nombre:", self.restaurante_nombre)
        print("Tipo de comida:", self.tipo_comida)

    def abrir_restaurante(self):
        print("El restaurante está abierto.")

class Heladeria(Restaurante):
    def __init__(self, restaurante_nombre, tipo_comida, sabores):
        super().__init__(restaurante_nombre, tipo_comida)

        self.sabores = sabores

    def mostrar_sabores(self):
        print("Sabores disponibles:")

        for sabor in self.sabores:
            print("-", sabor)

heladeria1 = Heladeria(
    "Helados Salta",
    "Helados",
    ["Chocolate", "Vainilla", "Frutilla"]
)

heladeria1.describir_restaurante()
heladeria1.abrir_restaurante()
heladeria1.mostrar_sabores()

"""EJERCICIO 5
1. Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
2. Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
personaje, al que le debe hacer el daño indicado por el atributo ataque.
3. Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
devuelva la cantidad cosechada"""

class Personaje:
    def __init__(self, vida, posicion, velocidad):
        self.vida = vida
        self.posicion = posicion
        self.velocidad = velocidad

    def recibir_ataque(self, daño):
        self.vida -= daño

        if self.vida <= 0:
            print("El personaje murió.")

    def mover(self, direccion):

        if direccion == "derecha":
            self.posicion += self.velocidad

        elif direccion == "izquierda":
            self.posicion -= self.velocidad

        print("Nueva posición:", self.posicion)

class Soldado(Personaje):
    def __init__(self, vida, posicion, velocidad, ataque):

        super().__init__(vida, posicion, velocidad)

        self.ataque = ataque

    def atacar(self, otro_personaje):
        otro_personaje.recibir_ataque(self.ataque)
        print("Ataque realizado.")

class Campesino(Personaje):
    def __init__(self, vida, posicion, velocidad, cosecha):

        super().__init__(vida, posicion, velocidad)

        self.cosecha = cosecha

    def cosechar(self):
        return self.cosecha
    
"""EJERCICIO 6
1. Cree una clase Usuario.
2. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
se guardan en un perfil de usuario.
3. Escriba un método describir_usuario() que muestre un resumen de la información del
usuario.
4. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno."""

class Usuario:
    def __init__(self, nombre, apellido, edad, email):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email

    def describir_usuario(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Edad:", self.edad)
        print("Email:", self.email)

    def saludar_usuario(self):
        print("Hola", self.nombre, self.apellido)

usuario1 = Usuario("Juan", "Perez", 20, "juan@gmail.com")
usuario2 = Usuario("Pablo", "Lopez", 22, "ana@gmail.com")
usuario3 = Usuario("María", "Rodriguez", 19, "carlos@gmail.com")

usuario1.describir_usuario()
usuario1.saludar_usuario()

print()

usuario2.describir_usuario()
usuario2.saludar_usuario()

print()

usuario3.describir_usuario()
usuario3.saludar_usuario()

"""EJERCICIO 7
Un administrador es un tipo de usuario con privilegios especiales.
1. Cree una clase Admin que herede de la clase
Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc.
2. Escriba un método mostrar_privilegios() que muestre el conjunto de privilegios del administrador, cree una
instancia de la clase y llame al método."""

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar_usuario(self):
        print("Hola", self.nombre, self.apellido)


class Admin(Usuario):
    def __init__(self, nombre, apellido, privilegios):

        super().__init__(nombre, apellido)

        self.privilegios = privilegios

    def mostrar_privilegios(self):

        print("Privilegios del administrador:")

        for privilegio in self.privilegios:
            print("-", privilegio)

admin1 = Admin(
    "Juan",
    "Perez",
    [
        "Puede postear en el foro",
        "Puede borrar un post",
        "Puede banear usuario"])

admin1.saludar_usuario()
admin1.mostrar_privilegios()

"""EJERCICIO 8
1. Escriba una clase Privilegios.
2. La clase debería tener un atributo, privilegios, que almacene una lista de strings
con los privilegios de manera similar a la del ejercicio 7.
3. Mueva el método mostrar_privilegios() de ese ejercicio a esta
clase.
4. Haga que una instancia de esta clase sea un atributo de la clase Admin.
5.Cree una nueva instancia de Admin y use el método para mostrar privilegios."""

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar_usuario(self):
        print("Hola", self.nombre, self.apellido)

class Privilegios:
    def __init__(self, privilegios):
        self.privilegios = privilegios

    def mostrar_privilegios(self):

        print("Privilegios:")

        for privilegio in self.privilegios:
            print("-", privilegio)

class Admin(Usuario):
    def __init__(self, nombre, apellido, privilegios):

        super().__init__(nombre, apellido)

        self.privilegios = Privilegios(privilegios)

admin1 = Admin(
    "Ana",
    "Lopez",
    [
        "Puede postear en el foro",
        "Puede borrar posts",
        "Puede banear usuarios"])

admin1.saludar_usuario()
admin1.privilegios.mostrar_privilegios()

"""EJERCICIO 9
1. Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela
al módulo actual.
2. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación
funcionó."""

from restaurante import Restaurante

mi_restaurante = Restaurante("Restaurante Nuevo", "Pizza")
mi_restaurante.describir_restaurante()
mi_restaurante.abrir_restaurante()
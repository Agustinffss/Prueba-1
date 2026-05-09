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
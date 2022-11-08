class Alumno:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.nota = int(input("Ingrese la nota: "))

    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def nota_al(self):
        if self.nota >= 3:
            print("Usted aprobó.")
        else:
            print("Usted rebrobó.")


alumno1 = Alumno()
alumno1.mostrar()
alumno1.nota_al()
alumno2 = Alumno()
alumno2.mostrar()
alumno2.nota_al()

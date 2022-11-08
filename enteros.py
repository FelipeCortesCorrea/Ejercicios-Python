class Calculadora:
  def __init__(self):
    self.valor1=int(input("ingrese un numero: "))
    self.valor2=int(input("ingrese otro numero: "))

  def suma(self):
    suma=self.valor1+self.valor2
    print("Resultado de la suma es: ", suma)

  def resta(self):
    resta=self.valor1-self.valor2
    print("Resultado de la resta es: ", resta)

  def multiplicacion(self):
    mult=self.valor1*self.valor2
    print("Resultado de la multiplicacion es: ", mult)

  def division(self):
    divicion=self.valor1/self.valor2
    print("Resultado de la division es: ", divicion)

  def mostrar(self):
    print("los resultados son: ")
    print("valor 1: ",self.valor1)
    print("valor 2: ",self.valor2)

resul=Calculadora()
resul.mostrar()
resul.suma()
resul.resta()
resul.multiplicacion()
resul.division()
    


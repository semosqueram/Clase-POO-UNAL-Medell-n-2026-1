class Calculos:
  def __init__(self):
    self.suma = 0
    self.x = 0
    self.y = 0
  def inicializar_variables(self, x_inicial, y_inicial):
    self.x = x_inicial
    self.y = y_inicial
  def realizar_calculos(self):
    self.suma = self.suma + self.x
    self.x = self.x + pow(self.y, 2)
    self.suma2 = self.suma + self.x / self.y
  def obtener_suma(self):
    return self.suma2
calculos = Calculos()
Calculos.inicializar_variables(int(input("ingresa el número x: ")),
int(input("ingresa el número y: ")))
Calculos.realizar_calculos()
print(f"El valor de la suma es: {Calculos.obtener_suma()}")

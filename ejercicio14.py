class Calculos:
  def calcular_cuadrado(self, num):
    cuadrado = float(pow(num, 2))
    return cuadrado

  def calcular_cubo(self, num):
    cubo = float(pow(num, 3))
    return cubo

    
calculos = Calculos()
num = float(input("Ingresa un número: "))
cuadrado = calculos.calcular_cuadrado(num)
cubo = calculos.calcular_cubo(num)
print("Número:", num)
print("Cuadrado:", cuadrado)
print("Cubo:", cubo)

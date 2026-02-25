import math
class Calculos:
  def calcular_longitud(self,r):
    longitud_circunferencia=float(2*math.pi*r)
    return longitud_circunferencia

  def calcular_area(self,r):
    valor_area=float(math.pi*pow(r,2))
    return valor_area

calculos=Calculos()
r=float(input("Ingresa el valor del radio del circulo: "))
l=calculos.calcular_longitud(r)
a=calculos.calcular_area(r)
print("La longitud de la circunferencia es: ",l)
print("El area del circulo es: ",a)


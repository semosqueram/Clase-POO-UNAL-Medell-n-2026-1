class Persona:
  def __init__(self, nombre, edad=0):
    self.nombre = nombre
    self.edad = edad
  def set_edad(self, edad):
    self.edad = edad
  def get_edad(self):
    return self.edad
  def get_nombre(self):
    return self.nombre

EdJuan = int(input("Ingresa la edad de Juan: "))
Juan = Persona("Juan", EdJuan)
Alberto = Persona("Alberto")
Ana = Persona("Ana")
Mamá = Persona("Mamá")
EdAlberto = (2/3) * Juan.get_edad()
EdAna = (4/3) * Juan.get_edad()
Edmamá = Juan.get_edad() + EdAlberto + EdAna
Alberto.set_edad(EdAlberto)
Ana.set_edad(EdAna)
Mamá.set_edad(Edmamá)
print(f"Las edades son:\n{Alberto.get_nombre()}:{Alberto.get_edad()}\n{Juan.get_nombre()}:{Juan.get_edad()}\n{Ana.get_nombre()}:{Ana.get_edad()}\n{Mamá.get_nombre()}:{Mamá.get_edad()}")

class Empleado:
    def __init__(self, horas_trabajadas, valor_hora,
      porcentaje_retencion=0.125):
      self.horas_trabajadas = horas_trabajadas
      self.valor_hora = valor_hora
      self.porcentaje_retencion = porcentaje_retencion
    def calcular_salario_bruto(self):
      return self.horas_trabajadas * self.valor_hora
    def calcular_retencion_fuente(self):
      salario_bruto = self.calcular_salario_bruto()
      return salario_bruto * self.porcentaje_retencion
    def calcular_salario_neto(self):
      salario_bruto = self.calcular_salario_bruto()
      retencion = self.calcular_retencion_fuente()
      return salario_bruto - retencion

      
horas = int(input("Ingrese las horas trabajadas en la semana: "))
valor_hora = float(input("Ingrese cuánto cobra semanalmente por hora: "))
retencion_input = float(input("Ingrese el porcentaje de retención: "))
retencion = retencion_input / 100
empleado1 = Empleado(horas, valor_hora, retencion)
salario_bruto = empleado1.calcular_salario_bruto()
retencion_valor = empleado1.calcular_retencion_fuente()
salario_neto = empleado1.calcular_salario_neto()
print(f"Salario bruto: ${salario_bruto:,.2f}")
print(f"Retención en la fuente ({retencion_input}%): ${retencion_valor:,.2f}")
print(f"Salario neto: ${salario_neto:,.2f}")


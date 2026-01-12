# Clase base
class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base


# Clase hija: Empleado de Tiempo Completo
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono

    def calcular_salario(self):
        return self.salario_base + self.bono


# Clase hija: Empleado de Medio Tiempo
class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, horas_trabajadas, tarifa_hora):
        super().__init__(nombre, 0)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_hora


# Prueba del sistema (Polimorfismo)
empleados = [
    EmpleadoTiempoCompleto("Carlos", 1000, 300),
    EmpleadoMedioTiempo("Ana", 80, 10)
]

for empleado in empleados:
    print(f"Empleado: {empleado.nombre} - Salario: ${empleado.calcular_salario()}")

class Analista:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

empleado1 = Analista("Juan", "Senior")
print(f"Empleado: {empleado1.nombre}, Nivel: {empleado1.nivel}")

empleado2 = Analista("Maria", "Junior")
print(f"Empleado: {empleado2.nombre}, Nivel: {empleado2.nivel}")
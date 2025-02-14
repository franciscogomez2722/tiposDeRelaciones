class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


class Medico(Persona):  # Herencia
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

class Enfermera(Persona):  # Herencia
    def __init__(self, nombre, edad, area):
        super().__init__(nombre, edad)
        self.area = area

# Uso
medico = Medico("Carlos", 45, "Cardiología")
enfermera = Enfermera("Laura", 30, "Pediatría")

medico.mostrar_info()
enfermera.mostrar_info()
